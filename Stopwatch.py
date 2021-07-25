import time

def countdown():
    t = 0
    while (1):
        min, sec = divmod(t,60) #divmod returns you a tuple of quotient and the remainder
        timer = f"{min}:{sec}"
        print(timer,end="\r")
        time.sleep(1)
        t += 1

countdown() 
