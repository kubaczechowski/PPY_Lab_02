# 1. Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym
# pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe to długość i
# szerokość podłogi. (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela
# oraz ilość paneli w opakowaniu. (10%)
import math


def calc(dluogsc_podlogi, szerokosc_podlogi,
         dlugosc_panela, szerokosc_panela, ilosc_paneli_w_opakowaniu):
    pole_podlogi = dluogsc_podlogi * szerokosc_podlogi * 1.1
    pole_panela = dlugosc_panela * szerokosc_panela
    return pole_podlogi / pole_panela / ilosc_paneli_w_opakowaniu


# 2. Napisz funkcję sprawdzającą czy podane liczby są liczbami pierwszymi w szybszy sposób niż w
# przykładzie. Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są
# liczbami pierwszymi. (10%)


def prime(*numbers):
    for no in numbers:
        is_no_prime = is_prime(no)
        if is_no_prime:
            print(f"{no} is prime")
        else:
            print(f"{no} is not prime")


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


prime(1, 2, 3, 4)


def szyfr_cezara(wiadomosc, klucz):
    letters = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ".lower()

    res = ""

    for letter in wiadomosc:
        if letters.__contains__(letter):
            res += letters[(letters.index(letter) + klucz) % len(letters)]
        if letters.upper().__contains__(letter):
            res += letters[(letters.index(letter.lower()) + klucz) % len(letters)]

    print(res)
    return res.lower()


szyfr_cezara("a", 70)
szyfr_cezara("A", 70)
