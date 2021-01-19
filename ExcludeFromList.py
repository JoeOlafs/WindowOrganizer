def __remove__(list):
    exclude = ['Taskbar', 'Overwolf Quick Launcher',
     'NVIDIA GeForce Overlay', 'Program Manager', '', '','','']
    for program in exclude:
        if program in list:
            list.remove(program)