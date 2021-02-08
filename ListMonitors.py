# Funciton to see number of displays connected to computer
import subprocess
import re

def Monitors():
     # Uses powershell to get info about connected monitors
     proc = subprocess.Popen(['powershell', 'Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams'], stdout=subprocess.PIPE)
     res = proc.communicate()
     monitors = re.findall('(?s)\r\nInstanceName\s+:\s(.*?)\r\n',res[0].decode("utf-8"))
     return monitors