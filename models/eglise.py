from utils import Formater
from exception import EmptyNameException
class Eglise: 
    id: int
    name: str
    
    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NullOrNegativeNumberException("The id can't be null or less than 0")
        else: 
            self.id = entered_id
            
    def set_name(self,n):
        if(Formater.chech_is_empty_string(n)):
            raise EmptyNameException("The church name can't be empty or null")
        else:
            self.name = n      