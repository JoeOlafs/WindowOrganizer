#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility

windows = Desktop(backend="uia").windows()
windowList = ([w.window_text() for w in windows])
ExcludeFromList.__remove__(windowList)
Visibility.__notMinimized__(windowList)
print(windowList)

for program in windowList:
    Window = gw.getWindowsWithTitle(program)[0]
    print(Window)