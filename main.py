import time
import random
import math

help = "Available Commands:\ntest\ngo to sleep\nchoose: rnd\nchoose: pi\nchoose: ans\nchoose: max\nchoose: min\n"


while True:
    CMD = input("CMD: ")
    
    if CMD.lower() == "help" or CMD.lower() == "list" or CMD.lower() == "what can i do":
        print(help)
    elif CMD.lower() == "test":
        print ("It works!")
    # אומר שהוא עובד אם אתה שואל אותו
    elif CMD.lower() == "go to sleep":
        print("ok")
        while True:
             CMD = input("")
             if CMD.lower() == "wake up!":
                 break
    # מתחיל סיום פרקטי בעת בקשה
    elif CMD.lower() == "choose: rnd":
        print (random.randint(-1000000000,1000000000)/1000000)
    elif CMD.lower() == "choose: pi":
        print (round(math.pi,6))
    elif CMD.lower() == "choose: ans":
       print(f"42.{random.randint(0,1000000)}")
    elif CMD.lower() == "choose: max":
       print(random.randint(100000,999999))
    elif CMD.lower() == "choose: min":
       print(random.randint(-100000,-999999))
       #מרנדם מספרים
    else: 
        print ("I haven't been programmed to proccess this yet\n(tip*: type help)")
    print()
# אומר אם אין תשובה