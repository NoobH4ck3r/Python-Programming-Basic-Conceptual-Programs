import random

comp_points, user_points = 0, 0
rounds = int(input("Enter the number of rounds you Want:\t"))
while rounds > 0:

    rounds -= 1
    lst = ["Snake", "Water", "Gun"]
    temp = random.choice(lst)
    choose_user = int(input("Choose a thing\n\n1.Snake\n\n2.Water\n\n3.Gun\n"))
    if (temp == "Snake" and choose_user == 3) or (temp == "Water" and choose_user == 1) or (temp == "Gun" and choose_user == 2):
        print("\nYou Won\n")
        print("Computer's Choice was", temp)
        user_points += 1
        print("\nYour points ", user_points, "Computer Points ", comp_points)
    elif (temp == "Snake" and choose_user == 2) or (temp == "Water" and choose_user == 3) or (temp == "Gun" and choose_user == 1):
        print("\nYou Lose\n")
        print("Computer's Choice was", temp)
        comp_points += 1
        print("\nYour points ", user_points, "Computer Points ", comp_points)
    elif (temp == "Snake" and choose_user == 1) or (temp == "Water" and choose_user == 2) or (temp == "Gun" and choose_user == 3):
        print("\nMatch Ties\n")
        print("Computer's Choice was", temp)
        print("\nYour points ", user_points, "Computer Points ", comp_points)
    else:
        print("Invlid Choice")

if comp_points > user_points:
    print("Computer is Winner")
elif user_points > comp_points:
    print("You are Winner")
else:
    print("Match Tie")
