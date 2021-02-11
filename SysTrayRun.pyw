import PySimpleGUIQt as sg
import Run

menu_def = ['BLANK',['Window Organizer','---','Run', 'Info', 'Stop']]

tray = sg.SystemTray(menu=menu_def, filename=r'appIcon.ico')

while True:
     menu_item = tray.Read()
     print(menu_item)
     if menu_item == 'Stop':
          break
     elif menu_item.startswith('Run'):
          try:
               Run.MainApp()
          except:
               sg.Popup('Error starting app', menu_item)
     elif menu_item == 'Info':
          sg.Popup('Menu Item Chosen', menu_item)
