import pygetwindow as gw



def __resize__(prog):
    print(prog[0])
    print(len(prog))

    if len(prog) == 0:
        print("No Windows Open")
    if len(prog) == 1:
        prog0 = str(prog[0])
        print(prog0)
        window = gw.getWindowsWithTitle(str(prog[0]))[0]
        window.maximize()
        print("Window Maximized")
    if len(prog) == 2:
        prog0 = gw.getWindowsWithTitle(str(prog[0]))[0]
        prog0.restore()
        prog0.moveTo(0,0)
        prog0.maximize()

        prog1 = gw.getWindowsWithTitle(str(prog[1]))[0]
        prog1.restore()
        prog1.moveTo(0,0)
        prog1.maximize()
    if len(prog) == 3:
        prog0 = gw.getWindowsWithTitle(str(prog[0]))[0]
        prog0.restore()
        prog0.resizeTo(960,1080)
        prog0.moveTo(-1920,0)
        print(prog0.size)

        prog1 = gw.getWindowsWithTitle(str(prog[1]))[0]
        prog1.restore()
        prog1.resizeTo(960,1080)
        prog1.moveTo(-960,0)
        print(prog1.size)

        prog2 = gw.getWindowsWithTitle(str(prog[2]))[0]
        prog2.restore()
        prog2.moveTo(0,0)
        prog2.maximize()
        print(prog2.size)