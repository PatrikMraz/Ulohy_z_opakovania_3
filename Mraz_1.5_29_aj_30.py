from random import * #naimportujem si knižnicu random
s = input('Zadaj slovo:') #do premennej s si uložím zadaný vstup
novy = '' #premennú novy nastavím ako string
novyy = '' #premennú novyy nastavím ako string
novyyy = '' #premennú novyyy nastavím ako string
for j in range(4): #for cyklus na vypísanie zmiešaných textov + ako sa vytvárajú
    if j == 1: #podmienka ak j sa rovná 1
        for i in range(len(s)): #for cyklus na skladanie textu
            ktory = randrange(len(s)) #vyberem náhodne písmeno
            print('Odstraňujem znak', s[ktory]) #vypíšem ktoré znaky odstraňujem
            novy = novy+s[ktory] #do premennej novy ukladám nový text
            print('Zatiaľ som vytvoril:', novy) #vypisujem čo som zatiaľ vytvoril
            s = s[:ktory]+s[ktory+1:] #do premennej s uložím text
            print('Ešte zostali tieto znaky:', s) #vypíšem znaky ktoré ostali
    if j == 2: #podmienka ak j sa rovná 2
        print('-----------------------') #oddelím text
        l = input('Zadaj také isté slovo:') #požiadam užívatela aby zadal znovu text
        for i in range(len(l)): #for cyklus na skladanie textu
            ktoryy = randrange(len(l)) #vyberem náhodne písmeno
            print('Odstraňujem znak', l[ktoryy]) #vypíšem ktoré znaky odstraňujem
            novyy = novyy+l[ktoryy] #do premennej novyy ukladám nový text
            print('Zatiaľ som vytvoril:', novyy) #vypisujem čo som zatiaľ vytvoril
            l = l[:ktoryy]+l[ktoryy+1:] #do premennej l uložím text
            print('Ešte zostali tieto znaky:', l)  #vypíšem znaky ktoré ostali
    if j == 3: #podmienka ak j sa rovná 3
        print('-----------------------') #oddelím text
        p = input('A ešte poslednýkrát zadaj to isté slovo:') #požiadam užívatela aby zadal znovu text
        for i in range(len(p)): #for cyklus na skladanie textu
            ktoryyy = randrange(len(p)) #vyberem náhodne písmeno
            print('Odstraňujem znak', p[ktoryyy]) #vypíšem ktoré znaky odstraňujem
            novyyy = novyyy+p[ktoryyy] #do premennej novyyy ukladám nový text
            print('Zatiaľ som vytvoril:', novyyy) #vypisujem čo som zatiaľ vytvoril
            p = p[:ktoryyy]+p[ktoryyy+1:] #do premennej p uložím text
            print('Ešte zostali tieto znaky:', p) #vypíšem znaky ktoré ostali  
print('Zamiešané slovo:', novy) #vypíšem zmiešaný text
print('Zamiešané slovo:', novyy) #vypíšem zmiešaný text
print('Zamiešané slovo:', novyyy) #vypíšem zmiešaný text
