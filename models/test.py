from eglise import Eglise
from offrande import Offrande

ofr = Offrande(12,234020,2,2024,1,404)
ofr.insert()

ls = Offrande.get_all_offrande()
print(len(ls))