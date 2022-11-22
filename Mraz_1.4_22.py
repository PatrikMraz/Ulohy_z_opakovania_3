from random import * #naimportujem si knižnicu random
heslo=' ' #premennú heslo si nastavím ako string
for i in range(8): #for cyklus na vypísanie hesla
    a=randint(97,122) #náhodne si vyberiem malé písmeno
    heslo=heslo+chr(a) #do premennej heslo si ukladám heslo
print(heslo) #vypíšem heslo

b=randint(65,90) #náhodne si vyberiem veľké písmeno
j=randint(1,7) #náhodne si vyberiem zy ktoré písmeno chcem nahradiť veľké písmeno
druhy=heslo[:j]+chr(b)+heslo[j+1:] #nahradím písmeno
print(druhy) #vypíšem heslo po nahradení písmen
