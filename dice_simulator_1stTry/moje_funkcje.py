# ZAMIANA NA PRAWIDLOWA KONCOWKE W ODPOWIEDZI NA PYTANIE O WIEK
def ilelat(x):
    if x == 1:
        return 'rok'
    elif 2 <= x <= 4:
        return 'lata'
    elif x >= 5:
        return 'lat'

# WPLATA NA KONTO W GRZE DICE_SIMULATOR
def deposit():
    while True:
        amount = input("Ile chcesz wplacic na swoje konto?: $")
        if amount.isdigit():
            if 0< int(amount):
                deposit_cash = amount
                print('---------------------------------------')
                print(f'Pomyslnie wplacono kwote ${amount} \n'
                      f'Stan twojego konta to: ${deposit_cash}'
                      f'')
                break
        else:
            print(f'Wpisano niepoprawna wartosc, Sprobuj ponownie')

# SPRAWDZEIE PRAWIDLOWEGO WPROWADZENIA PLCI W REJESTRACJI PROFILU ZAWODNIKA
def plec():
    while True:
        nazwa = input('Wybierz płeć (m/k):')
        print()
        if nazwa == "m" or nazwa == "M":
            plec_gracza = "Mezczyzna"
            return plec_gracza
           # break
        elif nazwa == "k" or nazwa == "K":
            plec_gracza = "Kobieta"
            return plec_gracza
           # break
        else:
           # print('Wprowadzono niepoprawne dane. Sprobuj ponownie.')
            return False