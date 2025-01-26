from playsound import playsound
import time
# playsound("E:/Codes/START_PYTHON/alarm_clock/a.mp3")

clear = "\033[23"
clear_return = "\033[H"

def alarm(minute, second):
    time_round = 0
    second += (minute*60)
    while(second):
        time.sleep(1)
        time_round+=1
        
        print(int(second/60),":",second%60)
        second-=1
    playsound("E:/Codes/START_PYTHON/alarm_clock/a.mp3")
        

minute = int(input("How many minute delay for alarm ??? "))
second = int(input("How many second delay for alarm ??? "))


alarm(minute,second)
