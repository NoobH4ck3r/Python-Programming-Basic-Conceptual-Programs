print("Enter no. of rows of your choice")
n = int(input(""))
print("Enter 1 for increasing pattern and 0 for decreasing pattern of stars")
m = bool(int(input("")))
if m == True:
    for i in range(1, n+1):
        print("*" * i)

else:
    for i in range(0, n):
        print("*" * (n-i))
