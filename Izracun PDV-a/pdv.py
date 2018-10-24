print "CIJENE ROIZVODA S PDV-om"
proizvodi = []
pdv_proizvoda = []
cijene_ukupno = []
def izracun_pdv(pdv_zadan, osnova):
    pdv = float(pdv_zadan / 100)
    pdv_kn = osnova * pdv
    return round(pdv_kn, 2)
def izracun_ukupno(osnovica):
    ukupno = osnovica + float(izracun_pdv(pdv_postotak, osnovica))
    return round(ukupno, 2)
add = int(raw_input("Koliko proivoda zelite upisati?"))
for x in range(add):
    proiz = float(raw_input("Cijena proizvoda: "))
    proizvodi.append(proiz)
    pdv_postotak = float(raw_input("Unesi postotak PDV-a (bez znaka %): "))
    pdv_proizvoda.append(izracun_pdv(pdv_postotak, proiz))
    cijene_ukupno.append(izracun_ukupno(proiz))
print "Lista cijena proizvoda je " + str(proizvodi)
print "Lista iznoda PDV-a proizvoda je " + str(pdv_proizvoda)
print "Lista cijena proizvoda je " + str(cijene_ukupno)



