# from menu import *
from moje_funkcje import *
# from Classy import *
# GAME INFO
nick = "GRACZ 1"
class Player():
    nick = ''
def menu():
    def registration():
        print('******** REJESTRACJA ********')
        while True:
            imie, nazwisko, wiek, nickname = input('Podaj imie: '), input("Podaj nazwisko: "), input("Podaj wiek: "), input("Podaj nickname: ")
            if imie.isalpha() == False or nazwisko.isalpha() == False or wiek.isdigit() == False or plec() == False:
                print('Podano nieprawidlowe dane. Sprobuj ponownie.')
            else:
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


                    Player.nick = nickname  #DOKONCZYC KLASE PLAYER !
                    Player.imie = imie
                    Player.nazwisko = nazwisko
                    Player.wiek = wiek
                    Player.plec = plec

                else:
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
        wybor = input('Wybierz w jakim trybie chcesz zaczac gre: ')
        if wybor == "g" or wybor == "G":
            pass
        if wybor == "z" or wybor == "Z":
            registration()




    run_dice_simulator()


def main_scene():
    print('\n -------------- DICE GAME SIMULATOR _____________ \n'
          f'           Jestes zalogowany jako:  {Player.nick}')
def main():
    menu()
    main_scene()
   # deposit()


main()