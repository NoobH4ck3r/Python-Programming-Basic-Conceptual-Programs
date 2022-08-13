import time


def file_searcher():
    time.sleep(5)
    with open("coroutines.txt", 'r') as f:
        temp=f.read()
    
    
    
    while(True):
        text=(yield)
        if text in temp:
            print(f"{text} found in file")
        else:
            print(f"{text} not found")



search=file_searcher()
next(search)
usr=input("Enter the text you want to find in the file:\t")
search.send(usr)
usr2=input("Enter anyother word in the file:\t")
search.send(usr2)