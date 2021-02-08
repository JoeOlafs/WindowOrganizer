import pygetwindow as gw

def __resize__(prog):
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
        prog0.moveTo(-7,0)
        prog0.maximize()

        prog1 = gw.getWindowsWithTitle(str(prog[1]))[0]
        prog1.restore()
        prog1.moveTo(-1928,0)
        prog1.maximize()
    if len(prog) == 3:
        prog0 = gw.getWindowsWithTitle(str(prog[0]))[0]
        prog0.restore()
        prog0.moveTo(-7,0)
        prog0.maximize()

        prog1 = gw.getWindowsWithTitle(str(prog[1]))[0]
        prog1.restore()
        prog1.resizeTo(976,1050)
        prog1.moveTo(-1928,0)

        prog2 = gw.getWindowsWithTitle(str(prog[2]))[0]
        prog2.restore()
        prog2.resizeTo(976,1050)
        prog2.moveTo(-968,0)
    if len(prog) == 4:
        prog0 = gw.getWindowsWithTitle(str(prog[0]))[0]
        prog0.restore()
        prog0.resizeTo(976,1050)
        prog0.moveTo(960,0)

        prog1 = gw.getWindowsWithTitle(str(prog[1]))[0]
        prog1.restore()
        prog1.resizeTo(976,1050)
        prog1.moveTo(-1928,0)

        prog2 = gw.getWindowsWithTitle(str(prog[2]))[0]
        prog2.restore()
        prog2.resizeTo(976,1050)
        prog2.moveTo(-968,0)

        prog3 = gw.getWindowsWithTitle(str(prog[3]))[0]
        prog3.restore()
        prog3.resizeTo(976,1050)
        prog3.moveTo(-7,0)
    if len(prog) == 5:
        prog0 = gw.getWindowsWithTitle(str(prog[0]))[0]
        prog0.restore()
        prog0.resizeTo(976,1050)
        prog0.moveTo(960,0)

        prog1 = gw.getWindowsWithTitle(str(prog[1]))[0]
        prog1.restore()
        prog1.resizeTo(976,1050)
        prog1.moveTo(-1928,0)

        prog2 = gw.getWindowsWithTitle(str(prog[2]))[0]
        prog2.restore()
        prog2.resizeTo(976,1050)
        prog2.moveTo(-968,0)

        prog3 = gw.getWindowsWithTitle(str(prog[3]))[0]
        prog3.restore()
        prog3.resizeTo(976,532)
        prog3.moveTo(-7,0)

        prog4 = gw.getWindowsWithTitle(str(prog[4]))[0]
        prog4.restore()
        prog4.resizeTo(976,532)
        prog4.moveTo(-7,525)