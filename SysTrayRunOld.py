import PySimpleGUIQt as sg
from PySimpleGUIQt.PySimpleGUIQt import EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
#import Run

menu_def = ['BLANK',['Window Organizer','---','&Run', 'Info', '&Stop', '&Close']]
tray = sg.SystemTray(menu=menu_def, filename=r'appIcon.ico')
tray.UnHide()

layout = [[sg.Text('Window Organizer')], [sg.Button('Close')]]
window = sg.Window('Window Organizer').Layout(layout)

tray_visible = True
window_visible = False
window_closed = False
#run_main = False

while True:
     if window_visible:
          event, values = window.Read()
          print(event)
          if event is None:
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_closed = True
          elif event == 'Close':
               print('Minimizing to tray')
               window.Hide()
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_closed = True
     if tray_visible:
          menu_item = tray.Read()
          if menu_item == 'Run' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
               print('Running Main')
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_closed = False
               #Run.run_main = True
               #print(Run.run_main)
          elif menu_item == 'Stop' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED:
               print('Stopping Main')
               #Run.run_main = False
               tray_visible = True
               window_visible = False
               window_closed = False
          elif menu_item == 'Info':
               tray_visible = True
               window_visible = True
               window_closed = False
               if window_closed:
                    window_closed = False
                    layout = [[sg.Text('Window Organizer')],[sg.Button('Close')]]
                    window = sg.Window('Window Organizer').Layout(layout)
               else:
                    window.Unhide()
          elif menu_item == 'Close':
               break