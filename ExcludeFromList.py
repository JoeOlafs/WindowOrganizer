# Function to remove selected programs from list of open programs
def __remove__(list):
    inList = []

    # List of programs and overlays that will not be arranged by the program
    exclude = ['Taskbar', 'Overwolf Quick Launcher',
     'NVIDIA GeForce Overlay', 'Screen share viewing options',
     'Program Manager', '']

    # Add programs that are open to a list, 
    for program in exclude:
        if program in list:
            inList.append(program)
    
    # Removes open programs that are in list to exclude from all open windows  
    for prog in inList:
        while prog in list:
            if prog in list:
                list.remove(prog)
