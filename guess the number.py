i = 9
number = 15
while (True) :
    i = i-1
    inp=int(input("Guess the number =\t"))
    print("\nTries remaining= ", i)
    if inp<number and i > 0:
        print("\nNumber is greater")
        continue
    if inp>number and i > 0:
        print("\nNumber is smaller")
        continue
    if i==0:
        print("\nGame over!!!\n")
        break
    else:
        print("\nCongrats you have guessed the number\n\nYou Took ",9-i,"Tries")
        break