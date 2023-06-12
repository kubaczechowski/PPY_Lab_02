import ssl
import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize

ssl._create_default_https_context = ssl._create_unverified_context

# Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
# Użyj reszty wierszy jako nagłówków ramki danych.
# Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.
# Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
with open('pliktextowy.txt', 'r') as file:
    lines = file.readlines()

url = lines[0].strip()
column_names = [name.strip() for name in lines[1:]]

df = pd.read_csv(url, header=None, names=column_names)

# Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)
wynik1 = ", ".join(df.columns)
print(wynik1)

# Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = f"Liczba wierszy: {df.shape[0]}, Liczba kolumn: {df.shape[1]}"
print(wynik2)


# Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
# wszystkie zmienne objaśniające powinny być w liscie.
# Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
# listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
# nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
# Nie pisz metody __str__.


# Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
class Wine:
    def __init__(self, explanatory_vars, response_var):
        self.explanatory_vars = explanatory_vars
        self.response_var = response_var

    def __repr__(self):
        return f"Wine(explanatory_vars={self.explanatory_vars}, response_var={self.response_var})"


explanatory_vars = df.columns[1:].tolist()
response_var = df.columns[0]
sample_wine = Wine(explanatory_vars, response_var)

wynik3 = sample_wine  # do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
# Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

# Zadanie 4.                             (3pkt)
# Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
# Nie podmieniaj listy, dodawaj elementy.
##Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniające i objaśniana.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
for _, row in df.iterrows():
    explanatory_vars = row[1:].tolist()
    response_var = row[0]
    wine = Wine(explanatory_vars, response_var)
    wineList.append(wine)

wynik4 = len(wineList)
print(wynik4)

# Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
# wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
# do wyniku przypisz zmienną objaśnianą z tego obiektu:
last_wine = wineList[-1]
repr_str = repr(last_wine)
new_wine = eval(repr_str)

wynik5 = new_wine.response_var
print(wynik5)

# Zadanie 6:                                                          (3pkt)
# Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
# Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
database_name = 'wines_jakub_czechowski.db'

conn = sqlite3.connect(database_name)
df.to_sql('wines', conn, if_exists='replace')
conn.close()

conn = sqlite3.connect(database_name)
query = "SELECT * FROM wines where TypeOf=3"
df_type_3 = pd.read_sql_query(query, conn)
conn.close()

wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"
wynik6 = df_type_3

print(wynik6.shape)

# Zadanie 7                                                          (1pkt)
# Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = LogisticRegression()

wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
# Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
# Znormalizuj dane objaśniające za pomocą:
# X = preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)
# Podział na zmienne objaśniające (X) i zmienną objaśnianą (y)
X = df.drop('TypeOf', axis=1)
y = df['TypeOf']

# Normalizacja danych objaśniających
X = normalize(X)

# Inicjalizacja modelu regresji logistycznej
model = LogisticRegression()

# Sprawdzian krzyżowy - LeaveOneOut
cross_val = LeaveOneOut()

# Wytrenowanie modelu i obliczenie dokładności
accuracy = cross_val_score(model, X, y, cv=cross_val).mean()

wynik8 = accuracy
print(wynik8)
