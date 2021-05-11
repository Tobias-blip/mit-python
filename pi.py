a = -2
b = -1
c = 0
d = 0
e = 1
f = 2
pi = 3
i = 0

while True:
    a = a + 4
    b = b + 4
    c = c + 4
    d = d + 4
    e = e + 4
    f = f + 4
    pi_et = 4 / (a * b * c) - 4 / (d * e * f)
    pi = pi_et + pi
    i += 1
    print(pi)