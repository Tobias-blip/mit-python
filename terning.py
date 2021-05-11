import math
import random

while True:

    i_alt = 0

    number_1 = 0

    number_2 = 0

    number_3 = 0

    number_4 = 0

    number_5 = 0

    number_6 = 0

    i = input("Hvor mange gange vil du kaste terningen?! ")

    i = int(i)

    while True:

        x = random.randint(1,6)

        i = i - 1

        print(x)

        if x == 1:
            number_1 += 1

        elif x == 2:
            number_2 += 1

        elif x == 3:
            number_3 += 1

        elif x == 4:
            number_4 += 1

        elif x == 5:
            number_5 += 1

        elif x == 6:
            number_6 += 1

        i_alt = x + i_alt

        if int(i) == 0:
            break

    print('--------------------------------')
    print("Tallet 1 blev kastet", number_1, "gange")
    print("Tallet 2 blev kastet", number_2, "gange")
    print("Tallet 3 blev kastet", number_3, "gange")
    print("Tallet 4 blev kastet", number_4, "gange")
    print("Tallet 5 blev kastet", number_5, "gange")
    print("Tallet 6 blev kastet", number_6, "gange")
    print("I alt", i_alt)
