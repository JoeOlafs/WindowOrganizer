import subprocess
import re

proc = subprocess.Popen(['powershell', 'Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorBasicDisplayParams'], stdout=subprocess.PIPE)
res = proc.communicate()
monitors = re.findall('(?s)\r\nInstanceName\s+:\s(.*?)\r\n',res[0].decode("utf-8"))
for m in monitors:
     print(m)