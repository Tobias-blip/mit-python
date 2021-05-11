import time
import random
muligheder = ["sten", "saks", "papir"]

din_score = 0
bot_score = 0

while True:
    n = random.randint(0,2)
    dit_valg = input('Sten, saks eller papir? ')
    bot_valg = muligheder[int(n)]
    if dit_valg == 'sten':
        print('Du valgte sten')
        time.sleep(1)
        if bot_valg == 'sten':
            print('Botten valgte også sten')
            time.sleep(1)
            print('Det var en uafgjort!')
            din_score = din_score + 1
            bot_score = bot_score + 1

        elif bot_valg == 'saks':
            print('Botten valgte saks')
            time.sleep(1)
            print('Du vandt!') 
            din_score = din_score + 1 

        else:
            print('Botten valgte papir')
            time.sleep(1)
            print('Du tabte')
            bot_score = bot_score + 1


    elif dit_valg == 'saks':
        print('Du valgte saks')
        time.sleep(1)
        if bot_valg == 'sten':
            print('Botten valgte sten')
            time.sleep(1)
            print('Du tabte')
            bot_score = bot_score + 1

        elif bot_valg == 'saks':
            print('Botten valgte også saks')
            time.sleep(1)
            print('Det var en uafgjort')  
            din_score = din_score + 1
            bot_score = bot_score + 1
        else:
            print('Botten valgte papir')
            time.sleep(1)
            print('Du vandt!')
            din_score = din_score + 1


    else:
        print('Du valgte papir')
        time.sleep(1)
        if bot_valg == 'sten':
            print('Botten valgte sten')
            time.sleep(1)
            print('Du vandt!')
            din_score = din_score + 1
            
        elif bot_valg == 'saks':
            print('Botten valgte saks')
            time.sleep(1)
            print('Du tabte')
            bot_score = bot_score + 1

        else:
            print('Botten valgte også papir')
            time.sleep(1)
            print('Det var en uafgjort')
            din_score = din_score + 1
            bot_score = bot_score + 1
    time.sleep(1)
    print('Du har', din_score, 'point, og botten har', bot_score, 'point')
    time.sleep(2)
