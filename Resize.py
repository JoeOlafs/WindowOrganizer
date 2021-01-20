import pygetwindow as gw

progList = []

def __resize__(prog):
    progList.append(prog)
    if len(progList) == 0:
        print("No Windows Open")
    elif len(progList) == 1:
        print(progList[0])
        #window = gw.getWindowsWithTitle(str(progList[0]))[0]
        #window.maximize()
        print("Window Maximized")
    elif len(progList) == 2:
        print("2 windows")