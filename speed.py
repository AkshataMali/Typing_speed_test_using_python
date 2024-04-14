from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
               error = error + 1
        except :
               error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s 
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

test =["This is my first repo","The first sentence of your paragraph should offer the reader an idea of the type of information they may expect to find when they read the rest." , 
        "My name is Akshata Mali","This is what i want"]
test1 = r.choice(test)
print("   ***** typing speed ****")
print(test1)
print()
print()
time_1 = time()
testinput = input(" Enter : ")
time_2 = time()


print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
print("Error : ",mistake(test1,testinput))
