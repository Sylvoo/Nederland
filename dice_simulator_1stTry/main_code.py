# from menu import *
from moje_funkcje import *
from Classy import *
# GAME INFO
# Jakies kiedys bylo

def first_log():
    def registration():
        print('******** REJESTRACJA ********')
        while True:
            imie, nazwisko, wiek, nickname, plecc = input('Podaj imie: '), input("Podaj nazwisko: "), input("Podaj wiek: "), input("Podaj nickname: "), input("Wybierz płeć (m/k): ")
            if imie.isalpha() == False or nazwisko.isalpha() == False or wiek.isdigit() == False or plec(plecc) == False:
                print('Podano nieprawidlowe dane. Sprobuj ponownie.')
            else:
                Player.imie = imie
                Player.nazwisko = nazwisko
                Player.nick = nickname
                Player.wiek = wiek
                Player.plec = plec(plecc)
                if 0 < int(wiek) < 18:
                    """def ilelat(x):
                        if x == 1:
                            return 'rok'
                        elif 2 <= x <=4:
                            return 'lata'
                        elif x >= 5:
                            return 'lat'
                            """
                    ile = 18 - int(wiek)
                    if int(wiek) <18:
                        print(" Jestes zbyt mlody aby korzystac z symulatora gry hazardowej!!\n "
                              f"Zapraszamy za {ile} {ilelat(ile)}, gdy juz bedziesz pelnoletni :D  ")
                        quit()


                else:
                    print()
                    print(f'********* Rejestracja przebiegla pomyslnie! *********\n '
                          f'Witamy Cie {nickname} na pokladzie!'
                          ' Zyczymy milej zabawy! ')
                 #   return nickname
                    break


    def run_dice_simulator():
        print('******** Witaj w symulatorze gry w kosci! ********')
        print()
        print(  '*_* Tryb Guest: Wybierz "g"\n'
                '^-^ Tryb Zawodnika: Wybierz "z"\n')
        while True:
            print()
            wybor = input('Wybierz w jakim trybie chcesz zaczac gre: ')
            if wybor == "g" or wybor == "G":
                print()
                print("----------Tryb tymczasowo nieaktywny, przepraszamy :< ---------- ")
                print()
            if wybor == "z" or wybor == "Z":
                registration()
                break
            else:
                print('Niepoprawne sformułowanie. Sprobuj jeszcze raz. Miales jedno zadanie... :P')

    run_dice_simulator()


def main_scene():
    print('\n -------------- DICE GAME SIMULATOR _____________ \n'
          f'           Jestes zalogowany jako: {Player.nick}')


def main():
    first_log()
    main_scene()
   # deposit()

main()
