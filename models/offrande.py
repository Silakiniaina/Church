from exception import *
class Offrande: 
    id: int
    montant: float
    numero_dimanche: int 
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
            
    def __init__(self,id,montant,nb_dim,annee,egl):
        self.set_id(id)
        self.set_montant(montant)
        self.set_numero_dimanche(nb_dim)
        self.set_annee(annee)
        self.set_id_eglise(egl)
        
    