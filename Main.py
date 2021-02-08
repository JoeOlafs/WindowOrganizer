from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility
import ResizeSingle
import ResizeDual
import ListMonitors
import Run

def __job__():
     # Gets all open windows, runs through the list of excluded programs and sorts by visibility
     windows = Desktop(backend="uia").windows()
     windowList = ([w.window_text() for w in windows])
     ExcludeFromList.__remove__(windowList)
     Visibility.__notMinimized__(windowList)

     # Checks for ammount of monitors
     monitors = ListMonitors.Monitors()

     # Checks if a new window has been opened or a window has been closed
     if len(windowList) == Run.numWindow:
          print('Number of window stays the same')
     else:
          Run.numWindow = len(windowList) # Updates the number of open windows
          print("List length: " + str(len(windowList)))
          # Additional checks when running in IDE
          for program in windowList:
               Window = gw.getWindowsWithTitle(program)[0]
               print(Window)
          windowList = tuple(windowList)

          #print('num Monitors: ' + str(len(monitors)))

          # Arranges windows depending on number of connected monitors
          count = 0
          if len(monitors) == 1:
               ResizeSingle.__resize__(windowList)
               print('Count: ' + str(count))
          if len(monitors) == 2:
               #ResizeSingle.__resize__(windowList) #for testint purposes, while List monitors is not working properly
               ResizeDual.__resize__(windowList)
               print('Count: ' + str(count))
               