import random
import os
import time

def clear(): 
    if os.name == 'nt':
        _ = os.system('cls')

while True:
    igen = input(":>> ")
    if igen == 'stop':
        break
    else:
        y = 0
        while y != 15:
            x = random.randint(1,6)
            print(x)
            y += 1
            clear()
        print(x)