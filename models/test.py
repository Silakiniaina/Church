from offrande import Offrande
from utils import *
from eglise import Eglise
from pret import Pret
from datetime import datetime

p = Pret(2,5,2024,54000000,1,1)
print(p.get_estimation())
