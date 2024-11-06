import time
from  datetime import date

# print(date.today())
print(time.strftime('%H:%M:%S'))
# hours = int(time.strftime('%H'))
hours = int(input("Enter hours \n"))
print("hourse : " , hours)
if hours >= 5 and hours <= 12:
    print("Good Morning!!")
elif hours >= 13 and hours <= 17:
    print("Good Afternoon !!")
elif hours >= 18 and hours <= 21:
    print("Good Evening !!")
else:
    print("Good Night !!")
#
# print(time.strftime('%M'))
# print(time.strftime('%S'))


# time.sleep(20)
# print(time.strftime('%H:%M:%S'))
