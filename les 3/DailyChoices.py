# Import
from time import sleep

#Morning
route = "waking up"

while route == "waking up":
    print("Your alarm is going off at 06:00")
    sleep(1)
    print("Do you GETUP or SNOOZE?:")
    wakeupchoice = input()

    if wakeupchoice == "GETUP":
        print("You woke up and get ready for school")
        route = "woke up on time"
    elif wakeupchoice == "SNOOZE":
        print("You continued to sleep and woke up late for school.")
        route = "late for school"

while route == "late for school":
    print("You do not have time to eat breakfast and quickly put on your clothing. Do you quickly double CHECK your bag or do you NOTCHECK your bag?")
    checkbag = input()
    if checkbag == "CHECK":
        print("You check your bag and see you forgot your earbuds. You quickly grab them and leave for school")
        route = "bag checked"
    elif checkbag == "NOTCHECK":
        print("You grab your bag and leave for school.")
        sleep(1)
        print("In the bus you want to grab your earbuds, but you realise you forgot them.")
        route = "bag wasn't checked"

while route == "woke up on time":
    print("You put on your clothes, eat breakfast and get ready for the rest of the day")
    sleep(1)
    print("Do you check your bag")

    checkbag = input()
    if checkbag == "CHECK":
        print("You check your bag and see you forgot your earbuds. You quickly grab them and leave for school")
        route = "bag checked"
    elif checkbag == "NOTCHECK":
        print("You grab your bag and leave for school.")
        sleep(1)
        print("In the bus you want to grab your earbuds, but you realise you forgot them.")
        route = "bag wasn't checked"

while route == "bag checked":
    print("Your day goes by smoothly. Your friend comes up to you and asks if you want to sit together")
    sleep(1)
    print("Do you SITWITHFRIEND or SITALONE?")
    seatingchoice = input()

    if seatingchoice == "SITWITHFRIEND":
        print("You agree to sit with your friend during the lessons")
        sleep(1)
        print("You're not lonely during the lessons!")
        route = "not lonely"
    elif seatingchoice == "SITALONE":
        print("You decide to sit alone during the lessons")
        sleep(1)
        print("Lmao, ur lonely. big L")
        route = "lonely"

while route == "bag not checked":
    print("Your day goes by with some problems. Your friend comes up to you and asks if you want to sit together")
    sleep(1)
    print("Do you SITWITHFRIEND or SITALONE?")
    seatingchoice = input()

    if seatingchoice == "SITWITHFRIEND":
        print("You agree to sit with your friend during the lessons")
        sleep(1)
        print("You're not lonely during the lessons!")
        route = "not lonely"
    elif seatingchoice == "SITALONE":
        print("You decide to sit alone during the lessons")
        sleep(1)
        print("Lmao, ur lonely. big L")
        route = "lonely"

while route == "not lonely":
    print("Its the end of the day and you return home with a good feeling")
    sleep(1)
    print("Do you MAKEHOMEWORK or GAME?")

    homeworkorgame = input()

    if homeworkorgame == "MAKEHOMEWORK":
        print("You make your homework and finish everything that has to be done.")
        route = "good ending"
    elif homeworkorgame == "GAME":
        print("You decide to game instead of making your homework.")
        sleep(1)
        print("You havent finished the homework for tomorrow.")
        route = "bad ending"

while route == "not lonely":
    print("Its the end of the day and you return home with a sad feeling")
    sleep(1)
    print("Do you MAKEHOMEWORK or GAME?")

    homeworkorgame = input()

    if homeworkorgame == "MAKEHOMEWORK":
        print("You make your homework and finish everything that has to be done.")
        route = "good ending"
    elif homeworkorgame == "GAME":
        print("You decide to game instead of making your homework.")
        sleep(1)
        print("You havent finished the homework for tomorrow.")
        route = "bad ending"

while route == "good ending":
    print("Good ending!")
    exit()

while route == "bad ending":
    print("Bad ending :(")
    exit()