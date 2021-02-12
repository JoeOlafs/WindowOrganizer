import PySimpleGUIQt as sg
from PySimpleGUIQt.PySimpleGUIQt import EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
import Run

menu_def = ['BLANK',['Window Organizer','---','&Run', 'Info', '&Stop', '&Close']]
tray = sg.SystemTray(menu=menu_def, filename=r'appIcon.ico')
tray.Hide()

layout = [[sg.Text('Window Organizer')],[sg.Button('Minimize to Tray')]]

window = sg.Window('Window Organizer').Layout(layout)

tray_visible = True
window_visible = False
window_closed = False
run_main = False

while True:
     if window_visible:
          event, values = window.Read()
          print(event)
          if event is None:
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_closed = True
          elif event == 'Minimize to Tray':
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
               window.UnHide()
               tray_visible = True
               window_visible = True
               window_closed = False
               run_main = True
               Run.MainApp()
               #while Run.MainApp():
               #     if menu_item == 'Stop' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED:
               #          run_main = False
               #          tray_visible = True
               #          window_visible = False
               #          window_closed = False
          elif menu_item == 'Close' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED:
               break