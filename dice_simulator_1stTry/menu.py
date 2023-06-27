def menu():
    def registration():
        while True:
            imie, nazwisko, wiek = input('Podaj imie: '), input("Podaj nazwisko: "), input("Podaj wiek: ")
            if imie.isalpha() == False or nazwisko.isalpha() == False:
                print('Podano nieprawidlowe dane. Sprobuj ponownie.')

            if wiek.isdigit():
                if 0 < int(wiek) < 18:
                    def ilelat(x):
                        if x == 1:
                            return 'rok'
                        elif 2 <= x <=4:
                            return 'lata'
                        elif x >= 5:
                            return 'lat'

                    ile = 18 - int(wiek)
                    if int(wiek) <18:
                        print(" Jestes zbyt mlody aby korzystac z symulatora gry hazardowej!!\n "
                              f"Zapraszamy za {ile} {ilelat(ile)}, gdy juz bedziesz pelnoletni :D  ")
                        quit()
                    else:
                        break
            else:
                print('Wprowadzono niepoprawne dane. Wprowadz je ponownie')

    def plec():
        while True:
            nazwa = input('Wybierz płeć (m/k): ')
            if nazwa == "m" or nazwa == "M":
                plec_gracza = "Mezczyzna"
                break
            elif nazwa == "k" or nazwa == "K":
                plec_gracza = "Kobieta"
                break
            else:
                print('Wprowadzono niepoprawne dane. Sprobuj ponownie.')

    def run():
        print('Witaj w symulatorze gry w kosci!')
        registration()
        plec()

    run()