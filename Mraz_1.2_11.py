import tkinter #naimportujem si plátno
canvas = tkinter.Canvas( bg='white', width=400, height=150) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno


def priletpismen(): #funkcia na vypísanie textu
    global i, x, slovo, txt, pozicia, ako #zadané premenné si nastavím ako globálne
    canvas.delete('pismeno') #vymažem text
    txt.append(canvas.create_text(x, 75,text=slovo[i], fill='blue',tag='pismeno',font='Arial 20 bold')) #do zoznamu uložím text
    if x>pozicia: #podmienka ak x je väčšie ako pozicia
        x=x-10 #premennú x zmenšujem o 10
        canvas.after(100,priletpismen) #volám funkciu priletpismen po 100 milisekundách
    if x==pozicia: #podmienka ak x sa rovná pozicia
        canvas.delete('pismeno') #vymažem text
        txt.append(canvas.create_text(x, 75,text=slovo[i], fill='blue',font='Arial 20 bold')) #do zoznamu uložím text
        i+=1 #premennú i zväčšujem o 1
        pozicia=pozicia+20 #premennú pozicia zväčšujem o 20
        x=300 #premennú x nastavím na 300
   
def run(): #funkcia ktorou volám funkciu na vypísanie textu
    global txt, slovo, i #zadané premenné si nastavím ako globálne
    slovo = entry1.get() #do premennej slovo si uložím zadané slovo
    txt= [] #premennú txt si nastavím ako zoznam
    i = 0 #premennú i nastavím na 0
    priletpismen() #volám funkciu priletpismen
    
x=300 #premennú x nastavím na 300
pozicia=100 #premennú pozicia nastavím na 100
txt = [] #premennú txt si nastavím ako zoznam
slovo = "" #premennú slovo nastavím ako string
i=0 #premennú i nastavím na 0
entry1=tkinter.Entry() #pripravím si vstup
entry1.pack() #vytvorím si vstup
button1=tkinter.Button(text='OK', command=run) #pripravím si tlačítko
button1.pack() #vytvorím si tlačítko