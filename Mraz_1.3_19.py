adresa=input('Zadaj url adresu:') #do premennej adresa si uložím zadanú url adresu
bodka=0 #premennú bodka nastavím na 0
bodkapoz=0 #premennú bodkapoz nastavím na 0
lomitko=0 #premennú lomitko nastavím na 0
lomitkopoz=0 #premennú lomitkopoz nastavím na 0
dvojbodka=0  #premennú dvojbodka nastavím na 0
lomitkopoz2=0 #premennú lomitkopoz2 nastavím na 0
for i in range(len(adresa)): #for cyklus na zistenie zadaných informácií
    if adresa[i]==':': #ak sa v adrese nachádza dvojbodka
        dvojbodka=i #uložím si jej pozíciu
    if adresa[i]=='/': #ak sa v adrese nachádza lomítko
        lomitko=lomitko+1 #do premennej lomitko ukladám počet lomítiek
        if lomitko==2: #podmienka ak lomitko sa rovná 2
            lomitkopoz2=i #uložím si pozíciu lomítka
        if lomitko==3: #podmienka ak lomitko sa rovná 3
            lomitkopoz=i #uložím si pozíciu lomítka
    if adresa[i]=='.': #ak sa v adrese nachádza bodka
        bodka=bodka+1 #premennú bodka zväčšujem o 1
        if bodka==2: #podmienka ak bodka sa rovná 2
            bodkapoz=i #do premennej bodkapoz uložím pozíciu

print(adresa[:dvojbodka]) #vypíšem protokol použitej služby
print(adresa[bodkapoz+1:lomitkopoz]) #vypíšem doménu najvyššej úrovne
print(adresa[lomitkopoz2+1:lomitkopoz]) #vypíšem doménovú adresu servera