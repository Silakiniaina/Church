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
    