while True:
    mængde = input('Mængde: ')
    valuta = input('(D)ollars eller (K)roner? ')
    if valuta == 'd' or 'D':
        kroner = int(mængde) * 6.06
        print(str(mængde), ' dollars er ', str(kroner), ' kroner værd')
    else:
        dollars = int(mængde) / 6.06
        print(str(mængde), ' kroner er ', str(dollars), ' dollars værd')