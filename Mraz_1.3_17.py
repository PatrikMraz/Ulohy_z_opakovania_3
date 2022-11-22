adresa=input('Zadaj url adresu:') #do premennej adresa si uložím zadanú url adresu
bodka=0 #premennú bodka nastavím na 0
zavinacpoz=0 #premennú zavinacpoz nastavím na 0
bodkapoz=0 #premennú bodkapoz nastavím na 0
bodkapoz2=0 #premennú bodkapoz2 nastavím na 0
for i in range(len(adresa)): #for cyklus na zistenie zadaných informácií
    if adresa[i]=='.': #ak sa v adrese nachádza bodka
        bodka=bodka+1 #premennú bodka zväčšujem o 1
        if bodka==2: #podmienka ak bodka sa rovná 2
            bodkapoz2=i #do premennej bodkapoz2 uložím pozíciu
        if bodka==3: #podmienka ak bodka sa rovná 3
            bodkapoz=i #do premennej bodkapoz uložím pozíciu
    if adresa[i]=='@': #ak sa v adrese nachádza zavinač
        zavinacpoz=i #do premennej zavinacpoz uložím pozíciu
        
print()
print()
print('Zadajte email:'+' '+adresa) #vypíšem adresu
print('TLD:'+' '+adresa[bodkapoz:len(adresa)]) #vypíšem doménu najvyššej úrovne
print('Server:'+' '+adresa[zavinacpoz+1:len(adresa)]) #vypíšem adresu mailového servera
print('User:'+' '+adresa[0:zavinacpoz]) #vypíšem meno používateľa
print('Domény:')                                                   ##
print('Doména 1. úrovne je:'+' '+adresa[bodkapoz+1:len(adresa)])     ###
print('Doména 2. úrovne je:'+' '+adresa[bodkapoz2+1:bodkapoz])       ###### vypíšem zoznam všetkých domén v poradí od domény prvej úrovne po doménu najnižšej úrovne
print('Doména 3. úrovne je:'+' '+adresa[zavinacpoz+1:bodkapoz2])   ##
    