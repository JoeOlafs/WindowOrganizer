"#WindowOrganizer" 
import pygetwindow as gw
from itertools import groupby
def isMin():
    #isMinimized
    return bool

openWindow = []
allWindows = [gw.getAllTitles()]
#print(gw.getActiveWindow().title)

#print(allWindows)
Window = allWindows[0]
print(type(allWindows))

for x in allWindows:
    openWindow = x
    print(openWindow)