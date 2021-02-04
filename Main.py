#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

import time
import RunScript

start = time.time()
errCount = 0

if __name__ == '__main__':
    while True:
        try:
            RunScript.__job__()
        except IndexError:
            print('IndexError')
            errCount += 1
        finally:
            timer = time.time()-start
            print('err count: ' + str(errCount))
            print(f'has been running for: '+ str(timer))
            time.sleep(1)
