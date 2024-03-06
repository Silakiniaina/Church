from models.data import Database
from models.utils import Formater
from datetime import date
from models.exception import *
class Eglise: 
    id: int
    name: str
    initial_solde: float
    date_last_fetch: date  
    
    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NumberException("The id can't be null or less than 0")
        else: 
            self.id = entered_id
            
    def set_name(self,n):
        if(Formater.chech_is_empty_string(n)):
            raise EmptyNameException("The church name can't be empty or null")
        else:
            self.name = n    
            
    def __init__(self,id: int,name: str,cur_solde: float,dt: date):
        self.set_id(id)
        self.set_name(name) 
        self.initial_solde = cur_solde
        self.date_last_fetch = dt
        
    @staticmethod
    def get_all_eglise():
        result = []
        con = None
        cur = None  
        rows = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM v_info_eglise"
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                temp = Eglise(row.__getitem__(0),row.__getitem__(1),row.__getitem__(2),row.__getitem__(3));
                result.append(temp)
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    @staticmethod
    def get_eglise_by_id(id: int):
        result = None
        con = None
        cur = None  
        row = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM v_info_eglise WHERE id_eglise= ?"
            values = (id)
            cur = con.cursor()
            cur.execute(query,values)
            row = cur.fetchone()
            if(row != None):
                result = Eglise(row.__getitem__(0),row.__getitem__(1),row.__getitem__(2),row.__getitem__(3));
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    