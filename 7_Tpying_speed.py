from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_start,time_end,user_input):
    time_delay=time_end-time_start
    time_R=round(time_delay,2)
    speed=len(user_input)/time_R
    return round(speed)

if __name__=='__main__':
    
    while True:
        ck=input(" Ready to test: yes(type 1) or no(type 2): ")
        if ck=='1':
            test=[
                "Did you hear about the first restaurant to open on the moon?It had great food, but no atmosphere.",
                "I went shopping for a pair of camouflage pants. But I couldn't find any.",
                "Life is what happens when you’re making other plans",
                "Now accepting applications for my fan club.",
                "Life is like a bus ride: sure, it’ll get you where you’re going, but you might get sneezed on."
                ]
            test1=r.choice(test)
            print("    *****Typing Speed*****   ")
            print(test1)
            print()
            print()
            time_1=time()
            test_input=input("Enter:")
            time_2=time()
            print("Speed: ",speed_time(time_1,time_2,test_input)," w/sec")
            print("Error: ",mistake(test1,test_input))
        
        elif ck=='2':
            print("Thank You")
            break
        else:
            print(" Wrong Input")
            break
    