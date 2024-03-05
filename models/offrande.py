from exception import *
from data import Database

class Offrande: 
    id: int
    montant: float
    numero_dimanche: int 
    nombre: int
    annee: int 
    id_eglise: int
     
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
            raise NumberException("The sunday_number can't be negative")
        elif(n > 52):
            raise NumberException("The sunday number can't be upper than 52")
        else: 
            self.numero_dimanche = n
    
    def set_annee(self, n: int):
        if(n < 2024):
            raise DateException("The year of offrande can't be lower than 2024")
        else:
            self.annee = n
    
    def set_id_eglise(self,entered_id: int):
        if(entered_id <= 0):
            raise NumberException("The id of the church can't be null or less than 0")
        else: 
            self.id_eglise = entered_id
            
    def __init__(self,id,montant,nb_dim,annee,egl,n):
        self.set_id(id)
        self.set_montant(montant)
        self.set_numero_dimanche(nb_dim)
        self.set_annee(annee)
        self.set_id_eglise(egl)
        self.set_nombre(n)
        
    def insert(self):
        con = None
        cur = None 
        try:
            con = Database.get_connection()
            query = f"INSERT INTO offrande(montant,numero_dimanche,annee,id_eglise,nombre) VALUES (?,?,?,?,?)"
            cur = con.cursor()
            values = (self.montant,self.numero_dimanche,self.annee,self.id_eglise,self.nombre)
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
    def get_all_offrande():
        result = []
        con = None
        cur = None  
        rows = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM offrande ORDER BY numero_dimanche ASC"
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                temp = Offrande(row.__getitem__(0),
                                row.__getitem__(1),
                                row.__getitem__(2),
                                row.__getitem__(3),
                                row.__getitem__(4),
                                row.__getitem__(5));
                result.append(temp)
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    