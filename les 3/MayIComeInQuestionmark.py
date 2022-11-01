import time
from datetime import date

def slowtext(string):
        for char in string:
                print(char, end='', flush=True)
        
slowtext("'Welcome!'")
time.sleep(1)
slowtext("\n'To enter you need to show us your ID.'")
time.sleep(1)
slowtext("\n'Do you show your ID?'")
show_ID = input(">").lower()

if show_ID == "yes":
        time.sleep(1)
        slowtext("\nenter your age:")
        r_b_y = input("\nbirthyear: ")
        r_b_m = input("\nbirthmonth: ")
        r_b_d = input("\nbirthday: ")

        b_y = int(r_b_y)
        b_m = int(r_b_m)
        b_d = int(r_b_d)
        today = date.today()

        c_y = (today.year)
        c_m = (today.month)
        c_d = (today.day)

        age = c_y - b_y - ((c_m, c_d) < (b_m, b_d))

        if age < 18:
                print("You cant enter since you are under 18")
        else:
                print("You can enter! Welcome")

# Handed in on 11/10