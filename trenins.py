def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2

    return rez

    
for skaitlis in range(1, 11, 2):        #range - funkcija, kas skaita skaitļus
   for otrs in range(1, 11, 2):  
       print("pirmais skaitlis:", skaitlis,"orais skaitlis", otrs, "rezultāts", rezultats(skaitlis, otrs))



def zvaigznites1 (skaitlis):
    for rindasNr in range(1, skaitlis+1):
        for zvaigzne in range(rindasNr):
             print("*", end="")
        print("")

def zvaigznites2(skaitlis):
    for rindasNr in range(1, skaitlis+1):
        print("*"*rindasNr)

zvaigznites1(7)
zvaigznites2(3)

skaitlis1 = 4
skaitlis2 = 3

print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis:", skaitlis2)
print("summa", rezultats(skaitlis1,skaitlis2))


