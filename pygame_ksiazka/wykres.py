# import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]


def srednia_ocen(oceny):
    if type(oceny) is not list:
        print("WPROWADZONO ZLE DANE ")

    suma = sum(oceny)
    srednia = suma / len(oceny)

    wynik = round(srednia, 2)
    return wynik

    legenda = ("1", "2", "3", "4", "5", "6")

    oceny_zliczone = [oceny.count(x) for x in range(1, 7)]

    plt.pie(oceny_zliczone, labels=legenda)
    plt.show()


print(srednia_ocen(x))

