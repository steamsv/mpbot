import functions
from process import Process
from settings import Settings
import psutil
import time

# p = Process(-1, '', '')
# while True:
#     pid = functions.get_pid_by_name(Settings.PNAME)
#     if pid == -1:
#         temp = Process(-1, name=Settings.PNAME, status='not found')
#     else:
#         try:
#             process = psutil.Process(pid)
#         except psutil.NoSuchProcess as e:
#             temp = Process(-1, name=Settings.PNAME, status='not found')
#         else:
#             temp = Process(pid, process.name(), process.status())
#     if temp.status != p.status:
#         functions.insert_into(temp)
#     p = temp
#     time.sleep(5)

pid = functions.get_pid_by_name(Settings.PNAME)
if pid == -1:
    temp = Process(-1, name=Settings.PNAME, status='not found')
else:
    try:
        process = psutil.Process(pid)
    except psutil.NoSuchProcess as e:
        temp = Process(-1, name=Settings.PNAME, status='not found')
    else:
        temp = Process(pid, process.name(), process.status())
functions.insert_into(temp)

