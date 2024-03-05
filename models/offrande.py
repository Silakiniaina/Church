from exception import *
class Offrande: 
    id: int
    montant: float
    numero_dimanche: int 
    annee: int 
    id_eglise: int
     
    def set_id(self,entered_id: int):
        if(entered_id <= 0):
            raise NullOrNegativeNumberException("The id can't be null or less than 0")
        else: 
            self.id = entered_id
            
    def set_montant(self,entered_montant: float):
        if(entered_montant < 0):
            raise NullOrNegativeNumberException("Le montant ne peut pas etre negatif")
        else:
            self.montant = entered_montant