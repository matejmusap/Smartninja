var2 = int(raw_input("Unesi ocjenu: "))
if var2 == 5:
    print "Odlican"
elif var2 == 4:
    print "Vrlo dobar"
elif var2 == 3:
    print "Dobar"
elif var2 == 2:
    print "Dovoljan"
elif var2 == 1:
    print "Nedovoljan"

while var2 != 0:
    if var2 >= 2:
        print "Prolazno!"
        break
    elif var2 == 1:
        print "Ponoviti!"
        break

var3 = []
var5 = float(0)
prosjek = float(0)
broj_predmeta = int(raw_input("Unesi broj predmeta: "))
for x in range(broj_predmeta):
    var4 = int(raw_input("Unesi ocjenu: "))
    var3.append(var4)
    var5 = float(var5 + var4)
prosjek = float(var5/broj_predmeta)
print var3
print prosjek
