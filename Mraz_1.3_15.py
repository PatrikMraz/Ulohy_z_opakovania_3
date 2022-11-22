slovo=input('Zadaj slovo:') #do premennej slovo si uložím zadané slovo
pocet=len(slovo) #do premennej pocet si uložím počet písmen v slove
for i in range(len(slovo)): #for cyklus na vypísanie slova podľa zadania
    print((pocet-i)*'.'+slovo[:i+1]) #vypíšem slovo pomocou rezu  a zadania s bodkami
