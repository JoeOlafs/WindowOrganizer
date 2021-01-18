from pywinauto import Desktop

windows = Desktop(backend="uia").windows()
windowList = ([w.window_text() for w in windows])
if 'Taskbar', '', 'Overwolf Quick Launcher' in windowList:
    windowList.remove('Taskbar', '', 'Overwolf Quick Launcher')
    print(windowList)
