vstup = input('Zadaj text:') #do premennej vstup si uložím zadaný vstup
sifra = '' #premennú sifra nastavím ako string
d_sifra = '' #premennú d_sifra nastavím ako string
for znak in vstup: #for cyklus na šifrovanie
    novyznak = znak #do premennej novyznak uložím znak
    if 'a' <= znak <= 'x': #podmienka ak znak sa nachádza medzi a a x
        novyznak = chr(ord(znak)+3) #uložím do premennej novyznak s posunom 1
    if znak == 'z': #podmienka ak znak sa rovná z
        novyznak = 'c' #do premennej novyznak uložím c
    if znak == 'x': #podmienka ak znak sa rovná x
        novyznak = a #do premennej novyznak uložím a
    if znak == 'y': #podmienka ak znak sa rovná y
        novyznak = 'b' #do premennej novyznak uložím b
    sifra = sifra+novyznak #do premennej sifra uložím novyznak
print(sifra) #vypíšem šifru


