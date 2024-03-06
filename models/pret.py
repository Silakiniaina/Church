from datetime import datetime
from exception import *
from models.croyant import Croyant
from models.data import Database
from models.eglise import Eglise

class Pret:
    id: int
    date_pret: datetime
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
    
    def __init__(self,id: int, dt: datetime, m: float, id_croyant: int,id_eglise):
        self.set_id(id)
        self.date_pret = dt
        self.set_montant(m)
        self.croyant = Croyant.get_croyant_by_id(id_croyant)
        self.eglise = Eglise.get_eglise_by_id(id_eglise)
    
    def insert(self):
        con = None
        cur = None 
        try:
            con = Database.get_connection()
            query = f"INSERT INTO pret(montant,date_pret,id_croyant,id_eglise) VALUES (?,?,?)"
            cur = con.cursor()
            values = (self.montant,self.date_pret,self.croyant.id,self.eglise.id)
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
    