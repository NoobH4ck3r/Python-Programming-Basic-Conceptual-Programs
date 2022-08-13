import time
from plyer import notification
import datetime
# initial = datetime.datetime.now()
# finalll= initial+datetime.timedelta(seconds=10)
# k = 0
# while(k < 45):
#     print("This is harry bhai")
#     # time.sleep(2)
#     k += 1
# print("While loop ran in", time.time() - initial, "Seconds")

# initial2 = time.time()
# for i in range(45):
#     print("This is harry bhai")
# print("For loop ran in", time.time() - initial2, "Seconds")


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)


# import datetime
old_time = datetime.datetime.now()
print(old_time)
new_time = old_time + datetime.timedelta(seconds=10)
print(new_time)
# print(initial)
# print(finalll)
while (True):
    # print("Loop")
    if datetime.datetime.now()>=new_time:
        print(datetime.datetime.now())
        notification.notify(title="Good work!",message="Take a 10 minute break! You have completed pomodoros so far")
        break

