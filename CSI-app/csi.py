characteristics = {
    "hair": {
        "black": "CCAGCAATCGC",
        "brown": "GCCAGTGCCG",
        "blonde": "TTAGCTATCGC"
    },
    "face": {
        "square": "GCCACGG",
        "round": "ACCACAA",
        "oval": "AGGCCTCA"
    },
    "eyes": {
        "blue": "TTGTGGTGGC",
        "green": "GGGAGGTGGC",
        "brown": "AAGTAGTGAC"
    },
    "gender": {
        "female": "TGAAGGACCTTC",
        "male": "TGCAGGAACTTC"
    },
    "race": {
        "white": "AAAACCTCA",
        "black": "CGACTACAG",
        "asian": "CGCGGGCCG"
    }
}

suspects = {
    "Eva": {
        "hair": "blonde",
        "face": "oval",
        "eyes": "blue",
        "gender": "female",
        "race": "white"
    },
    "Larisa": {
        "hair": "brown",
        "face": "oval",
        "eyes": "brown",
        "gender": "female",
        "race": "white"
    },
    "Matej": {
        "hair": "black",
        "face": "oval",
        "eyes": "blue",
        "gender": "male",
        "race": "white"
    },
    "Miha": {
        "hair": "brown",
        "face": "square",
        "eyes": "green",
        "gender": "male",
        "race": "white"
    }
}

suspect = {}

dna_file = open("dna.txt", "r")
dna = dna_file.read()
dna_file.close()
print dna

for characteristic, dna_code in characteristics.iteritems():
    for characteristics, code in dna_code.iteritems():
        if dna.find(code) != -1:
            suspect[characteristic] = characteristics
            break
print suspect
name = ""
for person, characteristic in suspects.iteritems():
    currentName = ""
    for characteristics, dna_code in characteristic.iteritems():
        if suspect[characteristics]:
            currentName = person
        else:
            currentName = ""
    if currentName:
        name = currentName
        break
print "%s is guilty for eating ice cream! " % name
