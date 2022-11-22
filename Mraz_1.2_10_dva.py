import tkinter #naimportujem si plátno
from random import * #naimportujem si knižnicu random
canvas = tkinter.Canvas(height=150,width=500,bg='white') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def slovo(): #funkcia, ktorou vykreslím slovo podľa zadania
    global x #premennú x nastavím ako globálnu
    global y #premennú y nastavím ako globálnu
    slovko = entry1.get() #do premennej slovko si uložím zadané slovo
    pocet=len(slovko) #do premennej pocet uložím počet písmen
    for znak in slovko: #for cyklus na vypísanie slova
        if pocet % 2 == 0: #podmienka ak pocet je párne číslo
            canvas.create_text(x,y,text=znak,font='Arial 30',fill='red') #vypíšem text
            x=x+30 #premennú x zväčšujem o 30
            pocet=pocet-1 #premennú počet zmenšujem o 1
        else:
             canvas.create_text(x,y,text=znak,font='Arial 30',fill='blue') #vypíšem text
             x=x+30 #premennú x zväčšujem o 30
             pocet=pocet-1 #premennú počet zmenšujem o 1
        
    
x=125 #premennú x nastavím na 125
y=75 #premennú y nastavím na 75

entry1 = tkinter.Entry() #pripravím si vstup
entry1.pack() #vytvorím si vstup

button1 = tkinter.Button(text='OK',command=slovo) #pripravím si tlačítko
button1.pack() #vytvorím si tlačítko

