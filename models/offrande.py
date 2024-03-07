import decimal
from models.exception import *
from models.eglise import Eglise
from models.data import Database
from models.utils import DateManagement

class Offrande: 
    id: int
    montant: float
    numero_dimanche: int 
    nombre: int
    annee: int 
    eglise: Eglise
     
    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NumberException("The id can't be null or less than 0")
        else:
            self.id = entered_id
            
    def set_montant(self,entered_montant: float):
        if(entered_montant < 0):
            raise NumberException("Le montant ne peut pas etre negatif")
        else:
            self.montant = entered_montant
            
    def set_nombre(self,n: int):
        if(n <= 0):
            raise NumberException("The id can't be null or less than 0")
        else: 
            self.nombre = n
            
    def set_numero_dimanche(self, n: int):
        if(n < 0):
            raise NumberException("The sunday number can't be null or less than 0")
        elif(n == 0):
            self.numero_dimanche = 52
            self.annee = self.annee - 1
        elif(n == 53): 
            self.numero_dimanche = 1
            self.annee = self.annee + 1
        else:
            self.numero_dimanche = n
    def set_annee(self, n: int):
        if(n < 1900):
            raise DateException("The year of offrande can't be lower than 1900")
        else:
            self.annee = n
    
    def set_id_eglise(self,entered_id: int):
        if(entered_id <= 0):
            raise NumberException("The id of the church can't be null or less than 0")
        else: 
            self.id_eglise = entered_id
            
    def get_eglise(self):
        return Eglise.get_eglise_by_id(self.id_eglise)
            
    def __init__(self,id,montant,nb_dim,annee,n,egl):
        self.set_id(id)
        self.set_montant(montant)
        self.set_annee(annee)
        if(str(egl).isdigit()):
            self.eglise = Eglise.get_eglise_by_id(egl)
        else:
            self.eglise = egl
        self.set_nombre(n)
        self.set_numero_dimanche(nb_dim)
        
    def insert(self,type=0):
        con = None
        cur = None 
        try:
            con = Database.get_connection()
            query = f"INSERT INTO offrande(montant,numero_dimanche,annee,id_eglise,nombre,type_offrande) VALUES (?,?,?,?,?,?)"
            cur = con.cursor()
            values1 = (self.montant,self.numero_dimanche,self.annee,self.eglise.id,self.nombre,type)
            cur.execute(query,values1)
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
    def get_last_offrande(num: int , annee: int):
        res = Offrande.get_offrande_by_numero_dimanche(num,annee)
        while(res == None):
            num -= 1
            if(num != 0): 
                res = Offrande.get_offrande_by_numero_dimanche(num,annee)
            else: 
                raise Exception("There was no offrande this year")
        return res 
   
    @staticmethod
    def get_all_offrande():
        result = []
        con = None
        cur = None  
        rows = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM offrande WHERE type_offrande = ? ORDER BY numero_dimanche ASC"
            cur = con.cursor()
            cur.execute(query,0)
            rows = cur.fetchall()
            for row in rows:
                temp = Offrande(row.__getitem__(0),row.__getitem__(1),row.__getitem__(2),row.__getitem__(3),row.__getitem__(4),row.__getitem__(5));
                result.append(temp)
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    @staticmethod
    def get_offrande_by_numero_dimanche(id: int,year: int):
        result = None
        con = None
        cur = None  
        row = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM offrande WHERE numero_dimanche= ? AND annee= ?"
            values = (id,year)
            cur = con.cursor()
            cur.execute(query,values)
            row = cur.fetchone()
            if(row != None):
                result = Offrande(row.__getitem__(0),row.__getitem__(1),row.__getitem__(2),row.__getitem__(3),row.__getitem__(4),Eglise.get_eglise_by_id(row.__getitem__(5)));
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    @staticmethod
    def get_portion(num_dim: int, year: int):
        result = 0.0
        con = None
        cur = None 
        row = None
        try: 
            con = Database.get_connection()
            query = f"SELECT ((t2.total-t1.total)/t1.total) as total FROM (SELECT sum(montant) as total FROM offrande WHERE numero_dimanche <= {num_dim} AND annee = {year-1})AS t1,(SELECT sum(montant) as total FROM offrande WHERE numero_dimanche <= {num_dim} AND annee = {year})AS t2";
            cur = con.execute(query)
            row = cur.fetchone()
            if(row != None):
                result = float(row.__getitem__(0))
        except Exception as e:
            raise e 
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    @staticmethod 
    def get_last_offrande_by_num_dim(n: int,year: int):
        result = None
        con = None
        cur = None  
        row = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM offrande WHERE numero_dimanche= ? AND annee <= ? ORDER BY annee DESC"
            if(n == 52):
                n = 1
                year = year + 1
            values = (n,year - 1,)
            cur = con.cursor()
            cur.execute(query,values)
            row = cur.fetchone()
            if(row != None):
                result = Offrande(row.__getitem__(0),row.__getitem__(1),row.__getitem__(2),row.__getitem__(3),row.__getitem__(4),Eglise.get_eglise_by_id(row.__getitem__(5)));
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    def predict(self,portion):
        result = None
        offrande_antetieur = Offrande.get_last_offrande_by_num_dim(self.numero_dimanche,self.annee)
        surplus = float(offrande_antetieur.montant) * portion
        next_valeur_offrande = float(offrande_antetieur.montant) + surplus
        self.eglise.initial_solde += decimal.Decimal(next_valeur_offrande)
        num_dim = 1 
        annee = self.annee
        if(self.numero_dimanche < 52): num_dim = self.numero_dimanche + 1
        elif(self.numero_dimanche == 52):
            num_dim = 1
            annee += 1
        result = Offrande(2,next_valeur_offrande,num_dim,annee,self.nombre,self.eglise)
        return result;           