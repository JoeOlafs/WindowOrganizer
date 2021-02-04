from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility

def __job__():
     windows = Desktop(backend="uia").windows()
     windowList = ([w.window_text() for w in windows])
     ExcludeFromList.__remove__(windowList)
     Visibility.__notMinimized__(windowList)
     print("List length: " + str(len(windowList)))