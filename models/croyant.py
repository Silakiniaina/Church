from datetime import datetime
from exception import *
from data import Database

class Croyant:
    id: int 
    first_name: str
    name: str
    date_of_birth: datetime
    email: str

    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NumberException("The id can't be null or less than 0")
        else: 
            self.id = entered_id
            
    def set_email(self,mail: str):
        if(not mail.__contains__("@") or not mail.__contains__(".com")):
            raise EmailException("The email must countains the character : '@' and '.com' ")
        else:
            self.email = mail
            
    def set_date_of_birth(self,dt: datetime):
        if(dt < datetime.now()):
            raise DateException("The date of birth couldn't be a future date")
        else:
            self.date_of_birth = dt
            
    def __init__(self,id: int, n: str, fn: str, dtn: datetime, mail: str):
        self.set_id(id)
        self.name = n
        self.first_name = fn 
        self.date_of_birth = dtn 
        self.email = mail
        
    @staticmethod 
    def authentificate(mail: str, pwd: str):
        result = None
        con = None
        cur = None  
        row = None
        try:
            con = Database.get_connection()
            query = f"SELECT * FROM croyant WHERE email='{mail}' AND mot_de_passe='{pwd}'"
            print(query)
            cur = con.cursor()
            cur.execute(query)
            row = cur.fetchone()
            if(row != None):
                result = Croyant(row.__getitem__(0),
                                 row.__getitem__(1),
                                 row.__getitem__(2),
                                 row.__getitem__(3),
                                 row.__getitem__(4));
        except Exception as e:
            print("There was an error while connecting")
        finally:
            if(cur != None): cur.close()
            if(con != None): con.close()
        return result