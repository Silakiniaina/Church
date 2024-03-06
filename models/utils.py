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
        date_en_cours = datetime(annee, 1, 1)
        dimanches_trouves = 0
        while dimanches_trouves != n:
            if date_en_cours.weekday() == 6:
                dimanches_trouves += 1
            if(dimanches_trouves != n):
                date_en_cours += timedelta(days=1) 

        return date_en_cours
    
    @staticmethod 
    def numero_dimanche(date_y, systeme=1):
        if isinstance(date_y, str):
            date_y = date.fromisoformat(date_y)
        jour_semaine = date_y.weekday()
        decalage = (jour_semaine - 6) % 7
        date_dimanche = date_y + timedelta(days=1 - decalage)
        if systeme == 2:
            if date_dimanche.isocalendar().week != 1:
                date_dimanche += timedelta(days=7)
        return date_dimanche.isoformat()
    