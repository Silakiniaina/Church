import calendar
from datetime import datetime
from datetime import date,timedelta

class Formater:
    
    @staticmethod
    def convert_string_to_date(s: str) -> datetime:
        return datetime.strptime(s,"%Y-%m-%d")
    
    @staticmethod
    def chech_is_empty_string(s: str) -> bool:
        result = False
        if(s.replace(" ","") == ""):
            result = True
        return result

class DateManagement:
    @staticmethod
    def date_dimanche_numero(n, annee):
        if n < 1 or n > 52:
            raise ValueError("Le chiffre n doit être compris entre 1 et 52 inclus.")
        date_en_cours = datetime(annee, 1, 1)
        dimanches_trouves = 0
        while dimanches_trouves != n:
            if date_en_cours.weekday() == 6:
                dimanches_trouves += 1
            if(dimanches_trouves != n):
                date_en_cours += timedelta(days=1) 

        return date_en_cours
    