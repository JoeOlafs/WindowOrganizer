import PySimpleGUIQt as sg
import Main
import traceback
import time
from threading import Thread

#Window Organizer
#Created by Johannes Olafsson - github.com/joeolafs
#Resizes and organizes open windows on your desktop, Runs from a System Tray Icon

menu_def = ['BLANK',['Window Organizer','---','&Run','&Info','&Stop','&Close']]
tray = sg.SystemTray(menu=menu_def, filename=r'appIcon.ico', tooltip='Window Organizer')
tray.UnHide()

layout = [[sg.Text('Window Organizer')],[sg.Button('Close')]]
window = sg.Window('Window Organizer').Layout(layout)

# Local Variables
tray_visible = True
window_visible = False
window_close = True
run_main = False
err_count = 0
start = time.time()

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
               while run_main == True:
                    menu_item_running = tray.Read(timeout = 2000)
                    if menu_item_running == 'Stop' or menu_item_running == sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
                         print('Stopping Main')
                         tray.UnHide()
                         tray_visible = True
                         window_visible = False
                         window_close = True
                         run_main = False
                    else:
                         try:
                              Main.__job__()    
                         except IndexError as err: # Ignores an common error in program, keeps track of how often it occurs
                              traceback.print_exc()
                              err_count += 1
                         except:
                              traceback.print_exc()
                              err_count += 1
                         finally: # Additional info while running in an IDE
                              timer = time.time()-start
                              print('err count: ' + str(err_count))
                              print(f'has been running for: '+ str(timer))
                              #time.sleep(1)
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
