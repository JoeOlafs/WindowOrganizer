import pygetwindow as gw


def __notMinimized__(list):
    for program in list:
        Window = gw.getWindowsWithTitle(program)[0]
#        print(Window)
        if Window.isMinimized:
            print(program + ' is minimized')
            list.remove(program)
        if Window.isMinimized == False:
            print(program + ' is not minimized')

#input into a list. then remove each item in that list