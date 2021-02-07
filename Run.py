#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

import time
import Main

start = time.time()
errCount = 0
numWindow = 0

# Program runs every second
if __name__ == '__main__':
    while True:
        try:
            Main.__job__()
        except IndexError as err: # Ignores common error in program, keeps track of how often it occurs
            errCount += 1
        finally: # Additional info while running in VS code
            timer = time.time()-start
            print('err count: ' + str(errCount))
            print(f'has been running for: '+ str(timer))
            time.sleep(1)
