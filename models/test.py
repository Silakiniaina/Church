from offrande import Offrande
from utils import *
from eglise import Eglise
from pret import Pret
from datetime import datetime

ls = Pret.get_all_pret_by_id_eglise(1)
print(len(ls))

