# This is a progrm which will determine that the entered number is armstrong or not e.g 153 = 1^3+5^3+3^3
usr_val=int(input("Enter the number greater than 100 and less than 1000:\t"))#Here we took vlaue form the key board
val_remainder1 = usr_val % 10   #Now we will make the remainder of the given number a name
a=usr_val/10                    #Now we will divide the value by ten to exclude the last digit of given number
val_remainder2 = int(a) % 10    #Now we will make the remainder of the given number a name
b= int(a)/10                    #Now we will divide the value by ten to exclude the last digit of given number
val_remainder3 = int(b) % 10    #Now we will make the remainder of the given number a name
if (val_remainder3**val_remainder1)+(val_remainder2**val_remainder1)+(val_remainder1**val_remainder1)==usr_val:
    print("Number is armstrong")
else:
    print("Number is normal")