import pygetwindow as gw

def __notMinimized__(list):
    isMinimized = []
    isNotMinimized = []
    for program in list:
        Window = gw.getWindowsWithTitle(program)[0]
        if Window.isMinimized:
            print(program + ' is minimized')
            isMinimized.append(program)
        if Window.isMinimized == False:
            print(program + ' is not minimized')
            isNotMinimized.append(program)

    for prog in isMinimized:
        if prog in list:
            list.remove(prog)

#input into a list. then remove each item in that list