foedselsaar = input('Hvilket aar blev du foedt? ')
foedselsdag = input('Har du haft foedselsdag i aar? ')
if foedselsdag == 'ja':
    alder = 2021 - int(foedselsaar)
else:
    alder = 2020 - int(foedselsaar)
print('Du er ' + str(alder) + ' aar gammel')
