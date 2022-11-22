from random import * #naimportujem si knižnicu random
heslo='' #premennú heslo si nastavím ako string
for i in range(8): #for cyklus na vykreslenie hesla
    if i<3: #podmienka ak i je menšie ako 3
        b=randint(65,90) #náhodne si vyberiem veľké písmeno
        heslo=heslo+chr(b) #do premennej heslo si uložím veľké písmeno
    if 3<=i<5: #podmienka ak i je väčšie rovné 3 a menšie ako 5
        c=randint(48,57) #náhodne si vyberiem číslo
        heslo=heslo+chr(c) #do premennej heslo si uložím číslo
    if i>=5: #podmienka ak i je väčšie rovné 5
        a=randint(97,122) #náhodne si vyberiem malé písmeno
        heslo=heslo+chr(a) #do premennej heslo si uložím malé písmeno
print(heslo) #vypíšem heslo