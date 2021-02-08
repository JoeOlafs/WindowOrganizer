import PySimpleGUIQt as sg
import Run

menu_def = ['BLANK',['Window Organizer','---','Run', 'Stop']]

tray = sg.SystemTray(menu=menu_def, filename=r'defaultIcon.ico')

while True:
     menu_item = tray.Read()
     print(menu_item)
     if menu_item == 'Stop':
          break
     elif menu_item == 'Run':
          Run.__run__()
