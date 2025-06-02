# work in progress, but basically counts down from the fromSecs (seconds to count down from) to 0
import time

def countdown(fromSecs):
    input("press enter to start timer")
    start = time.time()
    for i in range(fromSecs*10):
        current = time.time()
        sec = fromSecs-(round((current-start), 1))
        if sec<0:
            print(0)
            break
        print(f"\r{sec:.1f}", end="", flush=True)
        time.sleep(0.1)
#    input("press enter again if you want to pause the timer")
#    pause = time.time()

countdown(10)