import pygetwindow as gw

def __notMinimized__(list):
    isMinimized = []
    isNotMinimized = []
    for program in list:
        Window = gw.getWindowsWithTitle(program)[0]
        if Window.isMinimized:
            isMinimized.append(program)
        elif Window.isMinimized == False:
            isNotMinimized.append(program)

    for prog in isMinimized:
        if prog in list:
            list.remove(prog)