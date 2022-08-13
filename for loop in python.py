from msvcrt import getch


list1=["harry","carry",7,8,2,4,"Java",23,6]
for item in list1:
    if type(item) == int and item > 6:
        print(item)