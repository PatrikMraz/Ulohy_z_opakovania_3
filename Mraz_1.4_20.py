from random import * #naimportujem si knižnicu random
heslo='' #premennú heslo si nastavím ako string
for i in range(8): #for cyklus na vykreslenie hesla
    a=randint(97,122) #vyberám si náhodne malé písmeno 
    heslo=heslo+chr(a) #do premennej heslo ukladám písmená
print(heslo) #vypíšem heslo