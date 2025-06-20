# Project 6: Countdown Timer python project

import time

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
    print("Countdown completed!")

# Asking user to print amount of seconds to countdown

t = input("Enter the time in seconds: ")
countdown_timer(int(t))
