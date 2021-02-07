# Function to remove programs that have been minimized
import pygetwindow as gw

def __notMinimized__(list):
    isMinimized = []
    isNotMinimized = []

    # Arrange programs depening if they have been minimized or not
    for program in list:
        Window = gw.getWindowsWithTitle(program)[0]
        if Window.isMinimized:
            isMinimized.append(program)
        elif Window.isMinimized == False:
            isNotMinimized.append(program)

    # Remove programs that have been minimized from list of open programs
    for prog in isMinimized:
        if prog in list:
            list.remove(prog)