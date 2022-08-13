import requests
import jason
from win32com.client import Dispatch
import time

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)




data=requests.get(url="https://newsapi.org/v2/top-headlines?country=us&apiKey=c41a2e69b291454d80b03350003a17be")
result=data.json()
print(result['status'])


news = result['articles']

print(news)

speak("Welcome to the Wleed's News Channel")
speak("Here are the top ten news of United States")
speak("So our first news is ")
for i in range(0, 10):
    print(i)
    print(news[i]['title'])
    speak(news[i]['title'])
    print(news[i]['description'])
    speak(news[i]['description'])
    print(news[i]['content'])
    speak(news[i]['content'])
    if i >= 9:
        break
    time.sleep(2)
    if i == 8:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")


speak("Thanks for listening ! Have a nice day")
speak("Keep coding")
