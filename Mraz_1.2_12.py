veta=input('Napíš vetu:') #uložím si zadanú vetu do premenej veta
počet=0 #premennú počet nastavím na 0
slovo=0 #premennú slovo nastavím na 0
pozícia=0 #premennú pozícia nastavím na 0
for i in range(len(veta)): #for cyklus na zistenie počtu slov a dĺžku najdlhšieho slova,..
    if veta[i]==' ': #ak vo vete je medzera
        počet=počet+1 #premennú počet zväčšujem o 1
    počpís=len(veta)-(počet+1) #do premennej počpís uložím počet písmen
    slovo=počpís//4 +1 #do premennej slovo uložím najdl. slovo
    if i==slovo: #podmienka na akej pozícii je najdl. slovo
        pozícia=i #pozícia slova
        
print(počet+1) #vypíšem počet slov
print(slovo,pozícia) #vypíšem najdl. slovo a pozíciu