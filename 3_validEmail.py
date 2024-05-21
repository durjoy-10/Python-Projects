# a-z  durjoy_15432@gmail.com
# 0-9
# ._ time:1
# @  time :1
# .  pos:2,3

import re #Regex

email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

#here / for char search
#here ? for condition check

user_email=input("Enter your mail: ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
