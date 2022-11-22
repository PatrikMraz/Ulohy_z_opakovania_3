retazec=input('Zadaj reťazec dvoch spojených mien:') #do premennej retazec si uložím zadaný reťazec
pocet=len(retazec) #do premenej pocet si uložím počet písmen
meno='' #premennú meno si nastavím ako string
meno2='' #premennú meno2 si nastavím ako string
for znak in retazec: #for cyklus na vypísanie mien z ktorých je zložený reťazec
    if pocet % 2 == 0: #pdmienka ak je pocet párne číslo
        meno=meno+znak #do premennej meno si uložím písmeno z reťazca
        pocet=pocet-1 #premennú pocet si zmenšujem o 1
    else:
        meno2=meno2+znak #do premennej meno2 si uložím písmeno z reťazca
        pocet=pocet-1 #premennú pocet si zmenšujem o 1

print(meno) #vypíšem meno
print(meno2) #vypíšem druhé meno
        
        
        
    