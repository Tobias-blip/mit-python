foerste = input('Første tal: ')
tegn = input('+, -, *, /, ^. ') 
anden = input('Andet tal: ')

if tegn == '+':
    resultat = float(foerste) + float(anden)
elif tegn == '-':
    resultat = float(foerste) - float(anden)
elif tegn == '*':
    resultat = float(foerste) * float(anden)
elif tegn == '/':
    resultat = float(foerste) / float(anden)
else:
    resultat = float(foerste) ** float(anden)
print(resultat)
