#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

import time
import Main
import traceback
import ListMonitors

start = time.time()
numWindow = 0
monitors = ListMonitors.Monitors()

# The program runs constantly

def MainApp():
    #if __name__ == '__main__':
    errCount = 0
    while True:
        try:
            Main.__job__()
        except IndexError as err: # Ignores an common error in program, keeps track of how often it occurs
            traceback.print_exc()
            errCount += 1
        except:
            traceback.print_exc()
            errCount += 1
        finally: # Additional info while running in an IDE
            timer = time.time()-start
            print('err count: ' + str(errCount))
            print(f'has been running for: '+ str(timer))