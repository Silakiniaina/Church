from croyant import Croyant
from utils import Formater

dt = Formater.convert_string_to_date("2005-07-12")
c = Croyant.authentificate('sanda@gmail.com','admin')
if(c != None):
    print ("Connected as : ",c.name)
else: 
    print("Not connected")