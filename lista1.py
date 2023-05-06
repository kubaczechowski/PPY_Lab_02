# Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

# 1. Ile unikatowych elementów znajduje się w liście:
# 1 pkt
from collections import Counter
from random import random, randint

lista_1 = [0, 7, 8, 3, 3, 0, 7, 0, 3]
set = set(lista_1)
w_1 = "PODAJ WYNIK"
w_1 = len(set)
print(w_1)

# 2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
# na '0':
# 2 pkt
new = list(s_2)
new[randint(0, len(s_2) - 1)] = '0'
w_2 = "PODAJ WYNIK"
w_2 = ''.join(new)
print(w_2)

# 3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')}, 'c++'], ['word', 'excel']]

w_3 = "PODAJ WYNIK"
lista_3[0][0][0] = ('python', 'JS   ')
w_3 = lista_3
print(w_3)

# 4. Jakieg o typu dane z poniższych nie mogą być kluczami słownika?
# boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
# 1 pkt

w_4 = "PODAJ WYNIK"
w_4 = "list, set"  # tuple is immutable as well as other data types. key must be immutable
print(w_4)

# 5. Dla stringa wypisz
# ile razy pojawił się dany znak, w kolejności alfabetycznej.
# Użyj słownika - wynik również ma być słownikiem
# 2 pkt

s_5 = "ala ma kota imie ma macko"
counter = Counter(s_5)
counter.most_common()
w_5 = "PODAJ WYNIK"
w_5 = dict(sorted(counter.items()))
print(w_5)

# 6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
# jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
# Nie jeżeli nie wystąpił.
# 1 pkt
exists = 3 in w_5.values()
w_6 = "PODAJ WYNIK"
w_6 = exists
print(w_6)


# 7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
# i zwróci True lub False ( jest/ nie jest)
# pomiń znaki nie będące literami.
# 3pkt

def palindrom(s):
    res = ''
    for ele in s:
        if ele.isalpha():
            res += ele

    res = res.lower()

    for idx, character in enumerate(res):
        if character != res[len(res) - idx - 1]:
            return False
    return True


s_7_1 = "Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


# 8. Napisz funkcję, która zwróci
# wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami,
# jednak jeżeli liczba jest podzielna przez:
# trzy – zamiast liczby mamy „Fizz”,
# pięć – zamiast liczby mamy „Buzz”,
# trzy i pięć zamiast liczby mamy „FizzBuzz”.
# wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
# BEZ spacji
# 2 pkt

def fizzbuzz(n):
    res = ''
    for no in range(n):
        if no % 3 == 0 and no % 5 == 0:
            res += 'FizzBuzz, '
        elif no % 3 == 0:
            res += 'Fizz, '
        elif no % 5 == 0:
            res += 'Buzz, '
        else:
            res += str(no) + ", "

    return res


n_8 = 16
print(fizzbuzz(n_8))

# 9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# bez rekurencji:
# 3 pkt

n_9 = 6


def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    prev_1 = 1
    prev_2 = 1
    fib = 0

    for i in range(3, n + 1):
        fib = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = fib

    return fib


print(fibonacci(n_9))


# 10. Napisz funkcję, która dla podanej posortowanej listy
# zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
# lub zwróci None gdy nie ma elementu w liscie:
# 3 pkt


def binary_search(lista, e):
    left = 0
    right = len(lista) - 1
    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == e:
            return mid
        elif lista[mid] < e:
            left = (left + right) // 2 + 1
        else:
            right = (left + right) // 2 - 1
    return None


l_10 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
print(binary_search(l_10, 2))
