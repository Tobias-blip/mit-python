import os
import time
import random

tid = 5

high_score = 0

level = 0

def clear(): 
    if os.name == 'nt':
        _ = os.system('cls')

vil_spille = 'ja'

print('Velkommen til hukommelsespillet')
print('Det går ud på at huske det rigtige tal')
print('Om 10 sekunder kommer der et tal op på skærmen')
print('Det har du så 5 sekunder til at huske på')
print('Bagefter bliver du bedt om at skrive det tal der stod på skærmen før')
print('Hvis du husker rigtigt bliver det sværere, hvis du husker forkert taber du')
print('Held og lykke :)')
time.sleep(10)
clear()

while vil_spille == 'ja':
    i = 1
    while True:
        a = random.randint(1,i)
        print(a)

        time.sleep(int(tid))
        clear()

        gæt = input('Hvad var tallet? ')
        if gæt != str(a):
            print('Desværre, du døde')
            print('Det rigtige svar var ' + str(a))
            print('Du nåede til level ' + str(level))
            break
        else:
            clear()
        
        level += 1

        if i < 10000000:
            i = i * 10
        elif i < 1000000000000000:
            i = i * 2
        else:
            i = i * 10

    if level > int(high_score):
        high_score = level
    level = 0

    vil_ændre_tiden = input('Vil du ændre tiden? ')
    if vil_ændre_tiden == 'ja':
        tid = input('Hvor mange sekunder vil du have? ')

    print('Din high score er ' + str(high_score))
    vil_spille = input('Vil du spille igen? ').lower()
