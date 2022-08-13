import re


mystr = '''Hello Everybody this the thing where we wil show you some cool Email stuff
 in the string we have some cool emails for your intern ship on differnt companies like google mictosft etc
 stevejobs@gmail.com
 hermenhollerth@gmail.com Mya@gmail.com
 nothing@gmail.com'''

pattern = re.compile(r'[\w.]+[@][\w.]+')
match = pattern.findall(mystr)
for matches in match:
    print(matches)
    with open("Emails.txt","a") as a:
        a.write(f"{matches}\n")
