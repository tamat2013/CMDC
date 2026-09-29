import time
import random
import math

help = "Available Commands:\ntest\ngo to sleep\nchoose: rnd\nchoose: pi\nchoose: ans\nchoose: max\nchoose: min\n"


while True:
    CMD = input("CMD: ")
    
    if CMD == "help" or CMD == "list" or CMD == "What can I do":
        print(help)
    elif CMD == "test":
        print ("It works!")
    # אומר שהוא עובד אם אתה שואל אותו
    elif CMD == "go to sleep":
        print("ok")
        time.sleep(999999999)
    # מתחיל סיום פרקטי בעת בקשה
    elif CMD == "choose: rnd":
        print (random.randint(-1000000000,1000000000)/1000000)
    elif CMD == "choose: pi":
        print (round(math.pi,6))
    elif CMD == "choose: ans":
       print(f"42.{random.randint(0,1000000)}")
    elif CMD == "choose: max":
       print(random.randit(100000,999999))
    elif CMD == "choose: min":
       print(random.randit(-100000,-999999))
       #מרנדם מספרים
    else: 
        print ("I haven't been programmed to proccess this yet\n(tip*: type help)")
    print()
# אומר אם אין תשובה