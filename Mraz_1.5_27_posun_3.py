vstup = input('Zadaj text:') #do premennej vstup si uložím zadaný vstup
sifra = '' #premennú sifra nastavím ako string
d_sifra = '' #premennú d_sifra nastavím ako string
for znak in vstup: #for cyklus na šifrovanie
    novyznak = znak #do premennej novyznak uložím znak
    if 'a' <= znak <= 'w': #podmienka ak znak sa nachádza medzi a a w
        novyznak = chr(ord(znak)+3) #uložím do premennej novyznak s posunom 3
    if znak == 'z':  #podmienka ak znak sa rovná z
        novyznak = 'c' #do premennej novyznak uložím c
    if znak == 'x': #podmienka ak znak sa rovná x
        novyznak = 'a' #do premennej novyznak uložím a
    if znak == 'y':  #podmienka ak znak sa rovná y
        novyznak = 'b' #do premennej novyznak uložím b
    sifra = sifra+novyznak #do premennej sifra uložím novyznak
print(sifra) #vypíšem šifru



for znak in sifra: #for cyklus na dešifrovanie
    novyznak = znak #do premennej novyznak uložím znak
    if 'a' <= znak <= 'y': #podmienka ak znak sa nachádza medzi a a y
        novyznak = chr(ord(znak)-3) #uložím do premennej novyznak s posunom 3
    if znak == 'c': #podmienka ak znak sa rovná c
         novyznak = 'z' #do premennej novyznak uložím z
    if znak == 'a': #podmienka ak znak sa rovná a
        novyznak = 'x' #do premennej novyznak uložím x
    if znak == 'b': #podmienka ak znak sa rovná b
        novyznak = 'y' #do premennej novyznak uložím y
    d_sifra = d_sifra+novyznak #do premennej d_sifra uložím novyznak

print(d_sifra) #vypíšem dešifru  

