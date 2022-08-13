import os

def soldier(path):
    with open("C:\\Users\\Dell\\Documents\\Programming\\Python\\Soldier\\test only\\folderorganizer.txt", "r") as omit:
        temp=omit.read()
    omit_list=temp.split("\n")
    lst = os.listdir(path)
    print(lst)
    i = 1
    for items in lst:
        if os.path.isdir(items):
            continue
        elif ".jpg" in items:
            os.rename(f"{path}\\{items}", f"{path}\\{i}.jpg")
            i += 1
            continue
        elif items==omit_list:
            continue
        else:
            os.rename(f"{path}\\{items}", f"{path}\\{items.capitalize()}")
            continue


usr_path = input("Enter the path of the folder you wnat to edit:\t")
os.chdir(usr_path)
print(os.getcwd())
soldier(usr_path)
print("Done!!!")
