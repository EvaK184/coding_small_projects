# tracking the time elapsed between clicks of the Enter key.
# Each key press is starting a new "lap" of the timer.
# Calculates the time for each lap and the total time.

import time

def stopwatch():
    input("Click enter to start the first lap.")
    startTime = time.time()
    lapNo = 1
    try:
        while True:
            try:
                lapStartTime = lapEndTime
            except:
                lapStartTime = startTime
            q = input("Click again to start a new lap. Or press \"q\" to close the program.\n"+"~"*10)
            if q == "q":
                print("Bye bye!")
                quit()
            lapEndTime = time.time()
            print("Lap No: %s\nLap time: %s\nTotal time: %s"%(lapNo, round(lapEndTime-lapStartTime, 2), round(lapEndTime-startTime, 2)))
            lapNo += 1
            print('~'*10)
    except KeyboardInterrupt:
        print("Bye bye!")
stopwatch()