vstup = input('Zadaj text:') #do premennej vstup si uložím zadaný vstup
sifra = '' #premennú sifra nastavím ako string
d_sifra = '' #premennú d_sifra nastavím ako string
for znak in vstup: #for cyklus na šifrovanie
    novyznak = znak #do premennej novyznak uložím znak
    if 'a' <= znak <= 'x': #podmienka ak znak sa nachádza medzi a a x
        novyznak = chr(ord(znak)+1) #uložím do premennej novyznak s posunom 1
    if znak == 'z': #podmienka ak znak sa rovná z
        novyznak = 'a' #do premennej novyznak uložím a
    sifra = sifra+novyznak #do premennej sifra uložím novyznak
print(sifra) #vypíšem šifru



for znak in sifra: #for cyklus na dešifrovanie
    novyznak = znak #do premennej novyznak uložím znak
    if 'a' <= znak <= 'x': #podmienka ak znak sa nachádza medzi a a x
        novyznak = chr(ord(znak)-1) #uložím do premennej novyznak s posunom 1
    if znak == 'a':  #podmienka ak znak sa rovná b
         novyznak = 'z' #do premennej novyznak uložím z
    d_sifra = d_sifra+novyznak #do premennej d_sifra uložím novyznak

print(d_sifra) #vypíšem dešifru   
