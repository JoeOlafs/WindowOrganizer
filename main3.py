from pywinauto import Desktop
import win32gui

#windows = Desktop(backend="uia").windows()
#print([w.windows_text() for w in windows])

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hex(hwnd), win32gui.GetWindowText(hwnd))

win32gui.EnumWindows(winEnumHandler, None)