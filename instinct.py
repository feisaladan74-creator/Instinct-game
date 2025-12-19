"""Instinct — simple terminal Treasure Hunt game

Controls: W = Up, S = Down, A = Left, D = Right
Run: python3 instinct.py
"""
import random

SIZE = 5
MOVES = 12
TRAPS = 4


def create_board():
    return [["·" for _ in range(SIZE)] for _ in range(SIZE)]


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def place_random():
    return (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def play():
    board = create_board()

    player = place_random()
    treasure = place_random()
    traps = []

    while treasure == player:
        treasure = place_random()

    while len(traps) < TRAPS:
        t = place_random()
        if t != treasure and t != player and t not in traps:
            traps.append(t)

    moves_left = MOVES

    print("🎮 TREASURE HUNT PRO")
    print("Find the treasure before you run out of moves!")
    print("Controls: W = Up | S = Down | A = Left | D = Right")
    print()

    while moves_left > 0:
        temp_board = create_board()
        temp_board[player[0]][player[1]] = "P"
        print_board(temp_board)

        print(f"Moves left: {moves_left}")

        distance = manhattan(player, treasure)
        if distance == 1:
            print("🔥 Very close!")
        elif distance <= 2:
            print("😉 Getting warmer...")
        else:
            print("❄️ Cold...")

        move = input("Move (W/A/S/D): ").strip().lower()

        x, y = player

        if move == "w" and x > 0:
            x -= 1
        elif move == "s" and x < SIZE - 1:
            x += 1
        elif move == "a" and y > 0:
            y -= 1
        elif move == "d" and y < SIZE - 1:
            y += 1
        else:
            print("❌ Invalid move!")
            continue

        player = (x, y)

        if player in traps:
            print("💀 You stepped on a trap! Game Over!")
            print(f"Traps were at: {traps}")
            return

        if player == treasure:
            score = moves_left * 10
            print("🎉 YOU FOUND THE TREASURE!")
            print(f"🏆 Score: {score}")
            return

        moves_left -= 1

    print("⏰ Out of moves! You lost!")
    print(f"Treasure was at {treasure}")


def start():
    try:
        while True:
            play()
            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print("👋 Thanks for playing!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Exiting. Thanks for playing!")


if __name__ == "__main__":
    start()
