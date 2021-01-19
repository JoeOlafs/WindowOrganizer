#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

from pywinauto import Desktop

windows = Desktop(backend="uia").windows()
windowList = ([w.window_text() for w in windows])
print(windowList)
#if 'Taskbar', '', 'Overwolf Quick Launcher' in windowList:
 #   windowList.remove('Taskbar', '', 'Overwolf Quick Launcher')
  #  print(windowList)
