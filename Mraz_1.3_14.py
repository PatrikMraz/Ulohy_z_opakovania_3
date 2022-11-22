retazec=input('Zadaj reťazec dvoch spojených mien:') #do premennej retazec si uložím zadaný reťazec
pocet=len(retazec) #do premenej pocet si uložím počet písmen
i=1 #premennú i si nastavím na 1
y=-1 #premennú y si nastavím na -1
meno='' #premennú meno si nastavím ako string
meno2='' #premennú meno2 si nastavím ako string
while pocet>0: #kým pocet je väčší ako 0
        meno=meno+retazec[i:i+1] #do premennej meno si uložím písmeno z reťazca
        meno2=meno2+retazec[y+1:y+2] #do premennej meno2 si uložím písmeno z reťazca
        pocet=pocet-1 #premennú pocet si zmenšujem o 1
        i=i+2 #premennú i zväčšujem o 2
        y=y+2 #premennú y zväčšujem o 2
       
print(meno) #vypíšem meno
print(meno2) #vypíšem druhé meno