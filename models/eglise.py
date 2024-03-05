from data import Database
from utils import Formater
from exception import *
class Eglise: 
    id: int
    name: str
    
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
            
    def __init__(self,id,name):
        self.set_id(id)
        self.set_name(name)  
        
    @staticmethod
    def get_all_eglise():
        result = []
        con = None
        cur = None  
        rows = None
        try:
            con = Database.get_connection()
            query = "SELECT * FROM eglise"
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                temp = Eglise(row.__getitem__(0),row.__getitem__(1));
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
            query = "SELECT * FROM eglise WHERE id= ?"
            values = (id)
            cur = con.cursor()
            cur.execute(query,values)
            row = cur.fetchone()
            if(row != None):
                result = Eglise(row.__getitem__(0),row.__getitem__(1));
        except Exception as e:
            raise e
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result
    
    