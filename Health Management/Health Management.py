from pip import main


def Lock(taskk, personn):
    if taskk == 1:
        if personn == 1:
            with open("Health Management\Waleed's Diet.txt", "a") as f:
                f.write(str(getdate())+"\t" +
                        input("Enter the thing you have Eaten:\t")+"\n")
        elif personn == 2:
            with open("Health Management\Ali's Diet.txt", "a") as f:
                f.write(str(getdate())+"\t" +
                        input("Enetr the thing you have Eaten:\t"+"\n"))
        elif personn == 3:
            with open("Health Management\Hamaad's Diet.txt", "a") as f:
                f.write(str(getdate())+"\t" +
                        input("Enetr the thing you have Eaten:\t"+"\n"))
        else:
            print("No Client found Against This option")
    elif taskk == 2:
        if personn == 1:
            with open("Health Management\Waleed's Exercise.txt", "a") as f:
                f.write(str(getdate())+"\t" +
                        input("Enter the Exersise you have done:\t"+"\n"))
        elif personn == 2:
            with open("Health Management\Ali's Exercise.txt", "a") as f:
                f.write(str(getdate())+"\t" +
                        input("Enetr the Exersise you have done:\t"+"\n"))
        elif personn == 3:
            with open("Health Management\Hamaad's Exercise.txt", "a") as f:
                f.write(str(getdate())+"\t" +
                        input("Enetr the Exersise you have done:\t"+"\n"))
        else:
            print("No Client found Against This option")
    else:
        print("No task Found")


def retrive(taskk, personn):
    if taskk == 1:
        if personn == 1:
            with open("Health Management\Waleed's Diet.txt", "r") as f:
                print(f.read())
        elif personn == 2:
            with open("Health Management\Ali's Diet.txt", "r") as f:
                print(f.read())
        elif personn == 3:
            with open("Health Management\Hamaad's Diet.txt", "r") as f:
                print(f.read())
        else:
            print("No Client found Against This option")
    elif taskk == 2:
        if personn == 1:
            with open("Health Management\Waleed's Exercise.txt", "r") as f:
                print(f.read())
        elif personn == 2:
            with open("Health Management\Ali's Exercise.txt", "r") as f:
                print(f.read())
        elif personn == 3:
            with open("Health Management\Hamaad's Exercise.txt", "r") as f:
                print(f.read())
        else:
            print("No Client found Against This option")
    else:
        print("No task Found")


def getdate():
    import datetime
    return datetime.datetime.now()


main
print("This Progrm will manage your Health record e.g your diet and exercise")
personn = int(input("Choose Who are you\n\n1.Waleed\n\n2.Ali\n\n3.Hamaad\n"))
func = int(input(
    "\nchoose what you want to do\n1.Write The routine\n\n2.Retrive the Routine\n\n"))
if func == 1:
    taskk = int(input("\nChoose What you wnt to Lock\n\n1.Diet\n2.Exersise\n\n"))
    Lock(taskk, personn)
elif func == 2:
    taskk = int(
        input("\nChoose What you wnt to Retrive\n\n1.Diet\n2.Exersise\n\n"))
    retrive(taskk, personn)
else:
    print("Invlid function")
