#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop

from pywinauto import Desktop
import ExcludeFromList
#import Visibility

windows = Desktop(backend="uia").windows()
windowList = ([w.window_text() for w in windows])
print(windowList)
ExcludeFromList.__remove__(windowList)
print(windowList)
#Visibility.__isVisible__(windowList)