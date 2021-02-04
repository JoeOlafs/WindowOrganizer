#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility
import ResizeSingle
import ResizeDual
import ListMonitors
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

#monitors = ListMonitors.Monitors()

#windows = Desktop(backend="uia").windows()
#windowList = ([w.window_text() for w in windows])
#ExcludeFromList.__remove__(windowList)
#Visibility.__notMinimized__(windowList)
#print("List length: " + str(len(windowList)))

#for program in windowList:
#    Window = gw.getWindowsWithTitle(program)[0]
#    print(Window)


#print(windowList)
#if len(monitors) == 1:
#    ResizeSingle.__resize__(windowList)
#elif len(monitors) == 2:
#    ResizeDual.__resize__(windowList)
