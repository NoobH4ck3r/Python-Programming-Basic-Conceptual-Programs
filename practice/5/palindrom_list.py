lst=[3,8,100,83]


for items in lst:
    if items<=10:
        print(items)
    else:
        while(str(items) != str(items)[::-1]):
            items = int(items)
            items=items+1
            items=str(items)
        print(items)