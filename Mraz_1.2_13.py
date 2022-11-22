slovo = input('Zadaj slovo:') #do premennej slovo uložím zadané slovo
odsek = '' #do premennej odsek uložím string
for i in range(len(slovo)): #for cyklus na výpis slova podľa zadania
    print(odsek+slovo[i]) #vypisujem slovo podľa zadania
    odsek = odsek + ' ' #premennú odek posúvam o medzeru
