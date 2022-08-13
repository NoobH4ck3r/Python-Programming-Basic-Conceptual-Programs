from random import randint


def fake_table(number):
    wrong_index=randint(1,8)
    table=[i*number for i in range(1,11)]
    table[wrong_index]=table[wrong_index]+randint(1,11)
    print(table)
    return table






if __name__=="__main__":
    
    number=int(input("Enter the number of which you want to check the table of:\t"))
    given_table=fake_table(number)
    count=0
    for items in given_table:
        if items%number==0:
            continue
        else:
            print(f"The value at index {given_table.index(items)} is not correct it should be {(given_table.index(items)+1)*number} but it is {items}")
            count+=1
    if count==0:
        print("Table is correct")
    else:
        print(f"Table has {count} mistakes")
