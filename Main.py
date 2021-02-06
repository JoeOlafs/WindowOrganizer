from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility
import ResizeSingle
import ResizeDual
import ListMonitors

def __job__():
     windows = Desktop(backend="uia").windows()
     windowList = ([w.window_text() for w in windows])
     ExcludeFromList.__remove__(windowList)
     Visibility.__notMinimized__(windowList)
     print("List length: " + str(len(windowList)))

     # add if loop - int = len(windowList) stays the same -> do nothing
     # else - run rest of script and update int = len(windowList)
     for program in windowList:
          Window = gw.getWindowsWithTitle(program)[0]
          print(Window)
     monitors = ListMonitors.Monitors()
     print(len(monitors))
     #if len(monitors) == 1:
     #     ResizeSingle.__resize__(windowList)
     #if len(monitors) == 2:
     #     ResizeDual.__resize__(windowList)
