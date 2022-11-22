veta = input('Napíš vetu v slovenčine a ukončenú interpunkčným znamienkom:') #uložím si zadanú vetu do premenej veta

for i in range(len(veta)): #for cyklus na zistenie o akú vetu ide
    if veta[i]=='!': #ak sa vo vete nachádza výkričník
        print('Ide o rozkazovaciu vetu') #vypíšem o akú vetu ide
    if veta[i]=='.': #ak sa vo vete nachádza bodka
        print('Ide o oznamovaciu vetu') #vypíšem o akú vetu ide
    if veta[i]=='?': #ak sa vo vete nachádza otáznik
        print('Ide o opytovaciu vetu') #vypíšem o akú vetu ide
    