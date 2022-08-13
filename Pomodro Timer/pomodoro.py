import time as t
import pyttsx3
from plyer import notification


def speak(phrase):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(phrase)
    engine.runAndWait()
    print("Reminded successfully")
    print("Current time is ",t.ctime())


def notifier(event1,phrase):
    notification.notify(title=event1, message=phrase,)

if __name__ == "__main__":
    print("Welcome to the POMODORO program copyright Waleed Hassan\n\n")
    print("This program will remind you acoording to pomodoro technique while working on your PC to take rest")
    cycle=0
    main_counter=0
    print("\nStarting time is ",t.ctime())
    while(True):
        
        if cycle==4:
            notifier("Great Job!!", "You have worked for 2 hours its time for a break of 15 minutes")
            speak("YOu have worked for 2 hours its time for a break of 15 minutes")
            t.sleep(900)
            cycle=0
            notifier("Back to Work!!","Your fifteen minutes break has overed come back and do some more work")
            speak(f"Your fifteen minutes break has overed come back and do some more work")
            continue
        else:
            t.sleep(1500)
            notifier("Nice Work!!",f"You have worked for 25 minutes its time for a break of 5 minutes you have done {main_counter} pomodoros so far")
            speak(f"You have worked for 25 minutes its time for a break of 5 minutes you have done {main_counter} pomodoros so far")
            main_counter+=1
            cycle+=1
            t.sleep(300)
            notifier("Back to Work!!","Your 5 minutes break has overed come back and do another pomodoro")
            speak("Your five minutes break has overed come back and do another pomodoro")
            continue
            
    