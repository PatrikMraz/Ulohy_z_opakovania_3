meno=input('Zadaj meno:') #do premennej meno uložím zadané meno
meno2=input('Zadaj druhé meno:') #do premennej meno2 si uložím druhé meno
spol_meno='' #premennú spol_meno si nastavím ako string
for i in range(len(meno)): #for cyklus na vypísanie reťazca
    spol_meno=spol_meno+meno[i:i+1] #do premennej spol_meno ukladám písmeno z prvého mena
    spol_meno=spol_meno+meno2[i:i+1] #do premennej spol_meno ukladám písmeno z druhého mena
spol_meno=spol_meno+meno2[len(meno):len(meno2)] #doplním do reťazca chýbajúcu časť z dlhšieho reťazca
print(spol_meno) #vypíšem reťazec
    