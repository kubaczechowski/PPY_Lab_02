# pierwsze zadanie

# string1 = "Python 2023"
# string2 = "Python 2023"
# string3 = string1
#
# print(string1 == string2)  # True
# print(string2 == string3)  # True
# print(string3 == string1)  # True
#
# print(type(string1), hex(id(string1)))  # <class 'str'> 0x<jakies znaki>
# print(type(string2), hex(id(string2)))
# print(type(string3), hex(id(string3)))
#
# # Przypisanie trzeciej zmiennej nowego
# string3 = "Java 11"
#
# # Ponowne wykonianie punktu
# print(string1 == string2)
# print(string2 == string3)
# print(string1 == string3)
#
# print(type(string1), hex(id(string1)))
# print(type(string2), hex(id(string2)))
# print(type(string3), hex(id(string3)))

# drugie zadanie
# num1 = float(input("first no: "))
# num2 = float(input("second no: "))
#
# operator = input("choose operator (+, -, *, /): ")
#
# if operator == "+":
#     print(int(num1 + num2))
# elif operator == "-":
#     print(int(num1 - num2))
# elif operator == "*":
#     print(int(num1 * num2))
# elif operator == "/":
#     if num2 == 0:
#         print("cannot divide by zero")
#     else:
#         print(int(num1 / num2))
# else:
#     print("unknown operator")

# trzecie zadanie

# dictionaryWithQuestions = dict({
#     "podaj imie i nazwisko ": {
#
#     },
#     "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: *": {
#         "oglądanie telewizji",
#         "czytanie ksiazek",
#         "słuchanie muzyki"
#     },
#     "W jakich okolicznościach czytasz książki najczęściej? *": {
#         "podczas podróży",
#         "w czasie wolnym",
#         "w ogóle nie czytam"
#     },
#     "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? *": {
#         "chęć poszerzania wiedzy"
#         "fakt, że czytanie jest modne",
#         "czytanie to moje hobby"
#     },
#     "Po książki w jakiej formie sięgasz najczęściej? *" : {
#         "papierowej",
#         "e-booki",
#         "e-booki na telefonie"
#     },
#     "Ile książek czytasz średnio w ciągu roku? *" : {
#         "0",
#         "1",
#         "2-4"
#     },
#     "Jak często średnio czytasz książki? *" : {
#         "codziennie",
#         "raz w tygodniu",
#         "rzadziej niz raz w tygodniu"
#     },
#     "Po jakie gatunki książek sięgasz najczęściej? * " : {
#         "kryminały",
#         "naukowe",
#         "romanse"
#     }
#
#
# })
#
# for question, answers in dictionaryWithQuestions.items():
#     print(question)
#
#     for answer in answers:
#         print("-", answer)
#
#     user_answer = input("Twoja odpowiedź: ")
#
#     print(f"pytanie: {question}")
#     print(f"odpowiedź: {user_answer}")


# cwiczenia 3 zadanie 1
# userInput = input("Podaj liczby rozdzielone przecinkiem: ")
# input_split = userInput.split(",")
# input_split = [float(d) for d in input_split]  # list comprehension
#
# maxV = input_split[0]
# minV = input_split[0]
#
# for value in input_split:
#     if value > maxV:
#         maxV = value
#     if value < minV:
#         minV = value
#
# print(f"max {maxV}")
# print(f"min {minV}")

# zad 2
# import random
#
# cities_list = ["warsaw", "poznan", "gdynia",
#                "lodz", "krakow", "szczecin",
#                "bytom", "x", "y", "z"]
#
# visited_cities = []
#
# while len(visited_cities) < 10:
#     choice = random.choice(cities_list)
#     if choice not in visited_cities:
#         visited_cities.append(choice)
#
# print('Plan wycieczki:')
# for i, city in enumerate(visited_cities):
#     print(f'{i+1}. {city}')

#zad 3



