from random import randint


def player1(randnum):
    tries1 = 0
    while True:
        guesser1 = int(input("\n\nPlayer 1 guess the number:\t"))
        if guesser1 < randnum:
            print("Try again number is greater then entered number")
            tries1 += 1
            continue
        elif guesser1 > randnum:
            print("Try again  number is smaller than entered number")
            tries1 += 1
            continue
        elif guesser1 == randnum:
            tries1 += 1
            print(f"Congratulations you guessed the number in {tries1} tries")
            break
    return tries1


def player2(randnum):
    tries2 = 0
    while True:
        guesser2 = int(input("\n\nPlayer 2 guess the number:\t"))
        if guesser2 < randnum:
            print("Try again number is greater then entered number")
            tries2 += 1
            continue
        elif guesser2 > randnum:
            print("Try again  number is smaller than entered number")
            tries2 += 1
            continue
        elif guesser2 == randnum:
            tries2 += 1
            print(f"Congratulations you guessed the number in {tries2} tries")
            break
    return tries2


def winner(tries1, tries2):
    if tries1 > tries2:
        print("Player 2 wins")
    elif tries2 > tries1:
        print("Player 1 wins")
    elif tries1 == tries2:
        print("Match ties")


print("Welcome to the game\n")
min_val = int(input("Please enter the minimum value for range:\t"))
max_val = int(input("Please enter the maximum value for range:\t"))
winner(player1(randint(min_val, max_val)), player2(randint(min_val, max_val)))
