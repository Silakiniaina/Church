from datetime import datetime
import decimal
from exception import *
from croyant import Croyant
from data import Database
from eglise import Eglise
from offrande import Offrande
from utils import DateManagement

class Pret:
    id: int
    numero_dimanche: int
    annee: int
    montant: float 
    croyant: Croyant
    eglise: Eglise
    
    def set_montant(self,entered_montant: float):
        if(entered_montant < 0):
            raise NumberException("Le montant ne peut pas etre negatif")
        else:
            self.montant = entered_montant 

    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NumberException("The id can't be null or less than 0")
        else: 
            self.id = entered_id

    def set_numero_dimanche(self, n: int):
        if(n < 0):
            raise NumberException("The sunday number can't be null or less than 0")
        elif(n == 0):
            self.numero_dimanche = 52
            self.annee = self.annee - 1
        elif(n >= 53): 
            self.numero_dimanche = 1
            self.annee = self.annee + 1
        else:
            self.numero_dimanche = n
    
    def __init__(self,id: int,num_dim: int, annee:int, m: float, id_eglise: int,id_croyant: int):
        self.set_id(id)
        self.set_numero_dimanche(num_dim)
        self.annee = annee
        self.set_montant(m)
        self.croyant = Croyant.get_croyant_by_id(id_croyant)
        self.eglise = Eglise.get_eglise_by_id(id_eglise)
    
    def insert(self):
        con = None
        cur = None 
        try:
            con = Database.get_connection()
            query = f"INSERT INTO pret(montant,numero_dimanche,annee,id_croyant,id_eglise) VALUES (?,?,?,?,?,?)"
            cur = con.cursor()
            values = (self.montant,self.numero_dimanche,self.annee,self.croyant.id,self.eglise.id)
            cur.execute(query,values)
            con.commit()
            print("Insertion fait")
        except Exception as e:
            con.rollback()
            raise e       
        finally:
            if(cur != None): cur.close() 
            if(con != None): con.close()
        return
    
    @staticmethod
    def get_all_pret_by_id_eglise(id: int):
        result = []
        con = None
        cur = None  
        rows = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM pret WHERE id_eglise= ?"
            values = (id)
            cur = con.cursor()
            cur.execute(query,values)
            rows = cur.fetchall()
            temp = None
            for row in rows:
                temp = Pret(row.__getitem__(0),row.__getitem__(1),row.__getitem__(2),row.__getitem__(3),row.__getitem__(4),row.__getitem__(5))
                result.append(temp)
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    def get_estimation(self):
        eglise = Eglise.get_eglise_by_id(self.eglise.id)
        print("Demande de : ",self.montant," avec Solde initiale : ",eglise.initial_solde,"difference : ",eglise.initial_solde - self.montant)
        last_offrande = Offrande.get_last_offrande(self.numero_dimanche,self.annee)
        portion = Offrande.get_portion(self.numero_dimanche,self.annee)
        if(eglise.initial_solde >= self.montant):
            return DateManagement.date_dimanche_numero(self.numero_dimanche,self.annee)
        else:
            while(eglise.initial_solde < self.montant):
                next_offrande = last_offrande.predict(portion)
                eglise.initial_solde += decimal.Decimal(next_offrande.montant)
                print("Demande : ",self.montant, "Current solde : ",eglise.initial_solde," difference : ",eglise.initial_solde - self.montant) 
                last_offrande = next_offrande
            return DateManagement.date_dimanche_numero(last_offrande.numero_dimanche,last_offrande.annee)
        
        
    