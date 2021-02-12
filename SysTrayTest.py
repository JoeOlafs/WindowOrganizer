import PySimpleGUIQt as sg

def SysTray():
     menu_def = ['BLANK',['Window Organizer','---','&Run','Info','&Stop','Close']]
     tray = sg.SystemTray(menu = menu_def, filename = r'appIcon.ico')
     tray.UnHide()

     layout = [[sg.Text('Window Organizer')],[sg.Button('Close')]]
     window = sg.Window('Window Organizer').Layout(layout)

     tray_visible = True
     window_visible = False
     window_closed = True
     run_main = False

     while True:
          if window_visible:
               event, values = window.Read()
               print(event)
               