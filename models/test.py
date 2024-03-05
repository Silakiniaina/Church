from eglise import Eglise

ls = Eglise.get_all_eglise()
for i in range(len(ls)):
    print(f"{ls[i].name} {ls[i].id}")