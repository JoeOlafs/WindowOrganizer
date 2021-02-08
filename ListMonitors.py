import subprocess
import re

def Monitors():
     proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor'], stdout=subprocess.PIPE)
     res = proc.communicate()
     monitors = re.findall('(?s)\r\nDeviceID\s+:\s(.*?)\r\n',res[0].decode("utf-8"))
     return monitors