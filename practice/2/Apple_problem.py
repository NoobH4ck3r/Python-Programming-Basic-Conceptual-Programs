apples=int(input("Enter the number of apples you got:\t"))
min_value=int(input("Enter the minimum number of people you want to distribute apples among:\t"))
max_value=int(input("Enter the maximum number of people you want to distribute apples among:\t"))


for n in range(min_value,max_value+1):
    if min_value==max_value:
        print("Not a range")
    elif apples%n==0:
        print(f"{apples} number of apples are divisible on {n} people")
    else:
        print(f"{apples} number of apples are not divisible on {n} people")
