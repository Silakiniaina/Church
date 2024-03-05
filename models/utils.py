from datetime import datetime
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