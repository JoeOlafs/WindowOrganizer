from PySide2.QtWidgets import QSystemTrayIcon
import PySimpleGUIQt as sg
from PySimpleGUIQt.PySimpleGUIQt import EVENT_SYSTEM_TRAY_ICON_ACTIVATED
import Run

menu_def = ['BLANK',['Window Organizer','---','&Run', 'Info', '&Stop']]

tray = sg.SystemTray(menu=menu_def, filename=r'appIcon.ico')

while True:
     menu_item = tray.Read()
     print(menu_item)
#     if tray.Read(EVENT_SYSTEM_TRAY_ICON_ACTIVATED):
#          sg.Popup('ACTIVATED')
#          try:
#               Run.MainApp()
#          except:
#               sg.Popup('Error starting app')
     if menu_item == 'Stop':
          break
     elif menu_item.startswith('Run'):
          try:
               Run.MainApp()
          except:
               if QSystemTrayIcon.Trigger:
                    break
               sg.Popup('Error starting app', menu_item)
     elif menu_item == 'Info':
          sg.Popup('Menu Item Chosen', menu_item)
     elif menu_item == sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED:
          try:
               Run.MainApp()
          except:
               sg.Popup('Error starting app')
          if menu_item == sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
               break