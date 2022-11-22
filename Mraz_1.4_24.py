cisla='' #premennú cisla nastavím ako string
for i in range(49,58): #for cyklus na vypísanie čísiel
    if i-1==48: #podmienka ak i mínus 1 sa rovná 48
        cisla='"'+' '+cisla+chr(48)+' '+',' #uložím si prvé číslo + začiatok s úvodzovkami
    if i<=56: #podmienka ak i je menšie alebo rovné 56
        cisla=cisla+chr(i)+' '+',' #ukladám si čísla
    if i==57: #podmienka ak i sa rovná 57
        cisla=cisla+chr(57)+' '+'"' #uložím posledné číslo + koniec s úvodzovkami

print(cisla) #vypíšem čísla
        
        
    
