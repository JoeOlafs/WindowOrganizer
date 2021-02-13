import PySimpleGUIQt as sg

menu_def = ['BLANK',['Window Organizer','---','&Run','&Info','&Stop','&Close']]
tray = sg.SystemTray(menu=menu_def, filename=r'appIcon.ico')
tray.UnHide()

layout = [[sg.Text('Window Organizer')],[sg.Button('Close')]]
window = sg.Window('Window Organizer').Layout(layout)

tray_visible = True
window_visible = False
window_close = True
run_main = False

while True:
     if window_visible:
          event,values = window.Read()
          if event is None:
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_close = True
          elif event == 'Close':
               print('Minimize to Tray')
               window.Hide()
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_close = True
     if tray_visible:
          menu_item = tray.Read()
          if menu_item == 'Run' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
               print('Running Main')
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_close = True
               run_main = True
          elif menu_item == 'Stop' or menu_item == sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED:
               print('Stopping Main')
               tray.UnHide()
               tray_visible = True
               window_visible = False
               window_close = True
               run_main = False
          elif menu_item == 'Info':
               tray.Hide()
               tray_visible = False
               window_visible = True
               window_close = False
               if window_close:
                    layout = [[sg.Text('Window Organizer')],[sg.Button('Close')]]
                    window = sg.Window('Window Organizer').Layout(layout)
               else:
                    window.UnHide()
          elif menu_item == 'Close':
               break