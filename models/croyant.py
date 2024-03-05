from datetime import datetime
from exception import *

class Croyant:
    id: int 
    first_name: str
    name: str
    date_of_birth: datetime
    email: str

    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NullOrNegativeNumberException("The id can't be null or less than 0")
        else: 
            self.id = entered_id

    def set_email(self,mail: str):
        if(not mail.__contains__("@") or not mail.__contains__(".com")):
            raise EmailException("The email must countains the character : '@' and '.com' ")
        else:
            self.email = mail