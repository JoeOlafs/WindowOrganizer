from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility
import ResizeSingle
import ResizeDual
import Run

def __job__():
     # Gets all open windows, runs through the list of excluded programs and sorts by visibility
     windows = Desktop(backend="uia").windows()
     windowList = ([w.window_text() for w in windows])
     ExcludeFromList.__remove__(windowList)
     Visibility.__notMinimized__(windowList)

     # Checks for ammount of monitors

     monitorLen = len(Run.monitors)

     # Checks if a new window has been opened or a window has been closed
     if len(windowList) == Run.numWindow and len(Run.monitors) == monitorLen:
          #null = 'null'
          print('Number of window stays the same')
     else:
          Run.numWindow = len(windowList) # Updates the number of open windows
          print("List length: " + str(len(windowList)))
          # Additional checks when running in IDE
          for program in windowList:
               Window = gw.getWindowsWithTitle(program)[0]
               print(Window)
          windowList = tuple(windowList)

          # Arranges windows depending on number of connected monitors
          count = 0
          #while count <= 3:
          #     if monitorLen == 1:
          #          ResizeSingle.__resize__(windowList)
          #          count += 1
          #     if monitorLen == 2:
          #          ResizeDual.__resize__(windowList)
          #          count += 1