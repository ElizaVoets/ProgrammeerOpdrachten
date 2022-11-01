#Imports
import time
import random 
# Weekdagen

schooldag = True
huiswerk = True


weekdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]


day_picked = random.choice(weekdagen)

print(f"Het is "+ str(day_picked) + ". Moet je vandaag naar school?")
time.sleep(1)
decide_schoolday = input("Ja of Nee: ")
if decide_schoolday == "ja":
    schooldag = True
if decide_schoolday == "nee":
    schooldag = False

if schooldag == True:
        print("Pak je spullen en ga naar school")
        exit()
if schooldag == False:
    print("Je hoeft niet naar school.")
    time.sleep(1)
    print("Heb je huiswerk?")
    ds_Hw = input("Ja of nee: ")
    if ds_Hw == "ja":
        print("ga je huiswerk maken.")
    elif ds_Hw == "nee":
        print("Doe lekker wat je zelf wilt")
    else:
        print("Niet een antwoord.")

# Handed in on 11/10