#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

from pywinauto import Desktop
import ExcludeFromList

windows = Desktop(backend="uia").windows()
windowList = ([w.window_text() for w in windows])
print(windowList)
ExcludeFromList.__remove__(windowList)
print(windowList)
#if 'Taskbar' in windowList:
 #   windowList.remove('Taskbar', '', 'Overwolf Quick Launcher')
  #  print(windowList)
