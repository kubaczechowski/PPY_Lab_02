import random
from getpass import getpass

def get_player_move(player_name):
    """Pobiera ruch gracza"""
    while True:
        move = getpass(f"{player_name}, wpisz 'p' (papier), 'n' (nożyce), 'k' (kamień): ").lower()
        if move in ['p', 'n', 'k']:
            return move
        else:
            print("Nieprawidłowy ruch, spróbuj ponownie.")

def play_game(num_rounds, mode):
    """Główna funkcja gry"""
    players = []
    if mode == 'c':
        players = ['Komputer', input("Podaj nazwę gracza: ")]
    else:
        players = [input("Podaj nazwę gracza 1: "), input("Podaj nazwę gracza 2: ")]

    scores = {players[0]: 0, players[1]: 0}
    moves = ['p', 'n', 'k']

    for i in range(num_rounds):
        print(f"Runda {i+1}:")
        if mode == 'c':
            player1_move = random.choice(moves)
            player2_move = get_player_move(players[1])
        else:
            player1_move = get_player_move(players[0])
            player2_move = get_player_move(players[1])

        print(f"{players[0]} wybrał {player1_move}.")
        print(f"{players[1]} wybrał {player2_move}.")

        if player1_move == player2_move:
            print("Remis!")
        elif (player1_move == 'p' and player2_move == 'n') or \
             (player1_move == 'n' and player2_move == 'k') or \
             (player1_move == 'k' and player2_move == 'p'):
            print(f"{players[1]} wygrywa rundę!")
            scores[players[1]] += 1
        else:
            print(f"{players[0]} wygrywa rundę!")
            scores[players[0]] += 1

        print(f"Wynik po rundzie {i+1}: {players[0]} {scores[players[0]]} - {scores[players[1]]} {players[1]}\n")

    print("Wynik końcowy:")
    print(f"{players[0]} {scores[players[0]]} - {scores[players[1]]} {players[1]}")
    if scores[players[0]] > scores[players[1]]:
        print(f"{players[0]} wygrywa grę!")
    elif scores[players[0]] < scores[players[1]]:
        print(f"{players[1]} wygrywa grę!")
    else:
        print("Remis!")