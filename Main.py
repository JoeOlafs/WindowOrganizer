from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility
import ResizeSingle
import ResizeDual
import ListMonitors
import Run
import time

def __job__():
     windows = Desktop(backend="uia").windows()
     windowList = ([w.window_text() for w in windows])
     ExcludeFromList.__remove__(windowList)
     Visibility.__notMinimized__(windowList)
     monitors = ListMonitors.Monitors()

     if len(windowList) == Run.numWindow:
          print('Number of window stays the same')
     else:
          Run.numWindow = len(windowList)
          print("List length: " + str(len(windowList)))
          for program in windowList:
               Window = gw.getWindowsWithTitle(program)[0]
               print(Window)
          print(len(monitors))
          if len(monitors) == 1:
               ResizeSingle.__resize__(windowList)
          if len(monitors) == 2:
               ResizeDual.__resize__(windowList)