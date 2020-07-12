import time
from datetime import datetime

begintime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time.sleep(3)
endtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
begintime = datetime.strptime(begintime, '%Y-%m-%d %H:%M:%S')
endtime = datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
print endtime - begintime
print datetime.now().strftime("%Y%m%d%H%M%S")
