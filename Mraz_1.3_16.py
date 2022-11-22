slovo=input('Zadaj slovo:') #do premennej slovo si uložím zadané slovo
pocet=len(slovo) #do premennej pocet si uložím počet písmen slova
for i in range(len(slovo)): #for cyklus na vypísanie slova podľa zadania
    print(slovo[:i+1]+(pocet-i)*'.') #vypíšem slovo s bodkami podľa zadania
  