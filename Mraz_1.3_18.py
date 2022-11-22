rodnecislo = input('Rodné číslo:') #do premennej rodnecislo uložím zadané rodné číslo

roknarodenia = '19'+rodnecislo[:2] #do premennej roknarodenia si uložím roknarodenia pomocou rezov
if rodnecislo[2:4]>str(50): #podmienka ak mesiac narodenia je zväčšený o 50 a tým pádom je väčší ako 50
    mesiacnarodenia=int(rodnecislo[2:4])-50 #do premennej mesiacnarodenia si uložím mesiac narodenia
    pohlavie='Žena' #do premennej pohlavie si uložím pohlavie 
else:
    mesiacnarodenia=rodnecislo[2:4] #do premennej mesiacnarodenia si uložím mesiac narodenia
    pohlavie='Muž' #do premennej pohlavie si uložím pohlavie 

if rodnecislo[4:5]==str(0): #podmienka ak sa v dni narodenia nachádza 0
    dennarodenia=rodnecislo[5:6] #do premennej dennarodenia uložím deň narodenia
else:
    dennarodenia=rodnecislo[4:6] #do premennej dennarodenia uložím deň narodenia
    
print('Rodné číslo:'+' '+rodnecislo) #vypíšem rodné číslo
print('Dátum narodenia:'+' '+str(dennarodenia)+'.'+str(mesiacnarodenia)+'.'+str(roknarodenia)) #vypíšem dátum narodenia
print('Pohlavie:'+' '+pohlavie) #vypíšem pohlavie

