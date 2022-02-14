import time

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
    print("Timer completed !")
t = input("Please enter the time in seconds: ")
countdown(int((t)))