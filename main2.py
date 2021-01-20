from dragonfly import Window

allWindows = Window.get_all_windows()
openWindows = []
minWindows = []


for window in allWindows:
    if window.is_visible:
        openWindows.append(window)
        #print("true")


for window in openWindows:
    print(window.title)
    if window.is_maximized:
        print("MaxTrue")