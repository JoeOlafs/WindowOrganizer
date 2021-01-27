import pygetwindow as gw
from itertools import groupby
import vmi

def smaller_than_3(x):
     return x<3

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
          {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

a = [1,2,3,4]
group_obj = groupby(a,key=lambda x: x<3) #can also be the function defined above
for key, value in group_obj:
     print(key,list(value))
group_obj2 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj2:
     print(key,list(value))

mylist = [1,2,3]
for x in mylist:
     print(x)

notepadWindow = gw.getWindowsWithTitle('Untitled')[0]
if notepadWindow.isMinimized:
    print("true")
else:
    print("false")

obj = vmi.VMI().Win32_PnPEntity(ConfigManagerErrorCode=0)
displays = [x for x in obj if 'DISPLAY' in str(x)]
for item in displays:
     print(item)