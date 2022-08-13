import pickle
import requests
import os
r= requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


with open("data.txt", 'w') as index:
    index.write(r.text)


with open("data.txt", "r") as index:
    temp=index.read()


lst=temp.split('\n')


with open("data.pkl","wb") as f:
    pickle.dump(lst,f)


with open("data.pkl",'rb') as f:
    print(pickle.load(f))