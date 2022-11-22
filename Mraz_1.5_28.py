#Cézarova_šifra
vstup = input('Zadaj text:') #do premennej vstup si uložím zadaný vstup 
posun = input('Zadaj posun:') #do premennej posun si uložím posun o koľko posúvam
sifra = '' #premennú sifra nastavím ako string
for znak in vstup: #for cyklus na šifrovanie
    novyznak = znak #do premennej novyznak uložím znak
    if 'a' <= znak <= chr(ord('z')-int(posun)): #podmienka ak znak je medzi a a posunom ktorý zadám
        novyznak = chr(ord(znak)+int(posun)) ##uložím do premennej novyznak zo zadaným posunom 
    if znak >= chr(ord('z')-int(posun)): #podmienka ak znak je väčší alebo rovný ako z - zadaný posun
        novyznak = chr((ord(znak)-97+int(posun))%26+97) #uložím do premennej novyznak
    sifra = sifra+novyznak #do premennej sifra uložím novyznak
print(sifra) #vypíšem šifru

