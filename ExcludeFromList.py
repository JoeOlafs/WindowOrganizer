def __remove__(list):
    inList = []

    exclude = ['Taskbar', 'Overwolf Quick Launcher',
     'NVIDIA GeForce Overlay', 'Screen share viewing options',
     'Program Manager', '']

    for program in exclude:
        if program in list:
            inList.append(program)
    
    for prog in inList:
        while prog in list:
            if prog in list:
                list.remove(prog)
