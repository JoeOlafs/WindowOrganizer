from pywinauto import Desktop
import pygetwindow as gw
import ExcludeFromList
import Visibility
import ResizeSingle
import ResizeDual
import ListMonitors
import Run

def __job__():
     # Gets all open windows, runs through list of excluded programs and sorts by visibility
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
          Run.numWindow = len(windowList) # Updates number of open windows
          print("List length: " + str(len(windowList)))
          # Additional checks to see window info if running in VS code
          for program in windowList:
               Window = gw.getWindowsWithTitle(program)[0]
               print(Window)
          print(len(monitors))
          
          # Arrange windows depending on number fo connected monitors
          if len(monitors) == 1:
               ResizeSingle.__resize__(windowList)
          if len(monitors) == 2:
               ResizeDual.__resize__(windowList)
