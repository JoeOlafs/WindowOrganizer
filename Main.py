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

start = time.time()
monitors = ListMonitors.Monitors()

windows = Desktop(backend="uia").windows()
windowList = ([w.window_text() for w in windows])
ExcludeFromList.__remove__(windowList)
Visibility.__notMinimized__(windowList)
print("List length: " + str(len(windowList)))

#for program in windowList:
#    Window = gw.getWindowsWithTitle(program)[0]
#    print(Window)

print(time.time()-start)

#print(windowList)
#if len(monitors) == 1:
#    ResizeSingle.__resize__(windowList)
#elif len(monitors) == 2:
#    ResizeDual.__resize__(windowList)
