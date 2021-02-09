#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

import time
import Main

start = time.time()
numWindow = 0

# The program runs constantly

def __Main__():
    if __name__ == '__main__':
        errCount = 0
        while True:
            try:
                Main.__job__()
            except IndexError as err: # Ignores an common error in program, keeps track of how often it occurs
                errCount += 1
            finally: # Additional info while running in an IDE
                timer = time.time()-start
                print('err count: ' + str(errCount))
                print(f'has been running for: '+ str(timer))

__Main__()