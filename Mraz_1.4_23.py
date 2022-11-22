slovo='' #premennú slovo nastavím ako string
for i in range(98,123): #for cyklus na vypísanie abecedy
    if i-1==97: #podmienka ak i mínus 1 sa rovná 97
        slovo='"'+' '+slovo+chr(97)+' '+',' #uložím prvé písmeno abecedy + začiatok s úvodzovkami
    if i<=121: #podmienka ak i je menšie ako 121 alebo rovné 121
        slovo=slovo+chr(i)+' '+',' #ukladám abecedu
    else:
        slovo=slovo+chr(122)+' '+'"' #uložím koniec abecedy + koniec s úvodzovkami
print(slovo) #vypíšem abecedu
        