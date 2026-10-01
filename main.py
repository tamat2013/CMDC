import time
import random
import math
import datetime

help = "Available Commands:\ntest\ngo to sleep\nchoose: rnd\nchoose: pi\nchoose: ans\nchoose: max\nchoose: min\n"
timecheck = False

while True:
    CMD = input("CMD: ")
    CMD = CMD.lower()
    
    if CMD == "help" or CMD == "list" or CMD == "what can i do":
        print(help)
    elif CMD == "test":
        print ("It works!")
    # אומר שהוא עובד אם אתה שואל אותו
    elif CMD == "go to sleep":
        print("ok")
        while True:
             CMD = input("")
             if CMD == "wake up!":
                 break
    # מתחיל סיום פרקטי בעת בקשה
    elif CMD == "choose: rnd":
        print (random.randint(-1000000000,1000000000)/1000000)
    elif CMD == "choose: pi":
        print (round(math.pi,6))
    elif CMD == "choose: ans":
       print(f"42.{random.randint(0,1000000)}")
    elif CMD == "choose: max":
       print(random.randint(100000,999999))
    elif CMD == "choose: min":
       print(random.randint(-100000,-999999))
       #מרנדם מספרים
    elif CMD == "date":
        print (datetime.datetime.now())
        timecheck = True 
    elif CMD == "update" and timecheck:
        print("Updating...")
        print (datetime.datetime.now())
    else: 
        print ("I haven't been programmed to proccess this yet\n(tip* type: help)")
    print()

# אומר אם אין תשובה