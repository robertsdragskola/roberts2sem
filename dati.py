def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()


# ierakstit("mani sauc georgiāns")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()



# pierakstit_klat("domentāns georgiāns")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

# print(nolasit_visu())

def dabut_rindiņas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()
    


    for i in range(len(rindas)): 
        rindas[i] = rindas[i].strip()

    return rindas 

#saraksts = (dabut_rindiņas())
#print(saraksts)

ierakstit = ("sigma","https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Skibidi_toilet_screenshot.webp/237px-Skibidi_toilet_screenshot.webp.png")