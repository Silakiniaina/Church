from datetime import datetime
from exception import *

class Pret:
    id: int
    date_pret: datetime
    montant: float 
    id_croyant: int
    
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
    
    def __init__(self,id: int, dt: datetime, m: float, id_croyant: int):
        self.set_id(id)
        self.date_pret = dt
        self.set_montant(m)
        self.id_croyant = id_croyant
    