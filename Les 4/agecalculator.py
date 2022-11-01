import datetime
from datetime import date

today = date.today()


b_d = input("birthday:")
b_m = input("birthmonth:")
b_y = input("birthyear:")


def calc(year, month, day):
    birthday = datetime.date(int(year), int(month), int(day))
    age = (today - birthday)
    return age

    
print(calc(b_y, b_m, b_d))
