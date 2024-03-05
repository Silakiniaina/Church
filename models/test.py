from offrande import Offrande

ofr1 = Offrande.get_offrande_by_numero_dimanche(8,2023)
print("Taloha : "+str(ofr1.montant))
predict = ofr1.predict(0.06795)
print("Hoavy : "+str(predict.montant))

portion = Offrande.get_portion(5,2023)
print("Portion : ",portion)

