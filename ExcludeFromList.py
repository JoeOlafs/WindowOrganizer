def __remove__(list):
    exclude = ['Taskbar', 'Overwolf Quick Launcher',
     'NVIDIA GeForce Overlay', 'Screen share viewing options',
     'Program Manager', '', '','','']
    for program in exclude:
        if program in list:
            list.remove(program)

#input into a list. then remove each item in that list