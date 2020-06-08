import datetime
import time
t=datetime.datetime.now()
print(t)
print(t.strftime("%Y-%m-%d-%H-%M-%S-%M"))
print(t.strftime("%Y%m%d%H%M%S%M"))
print(t.year,t.month,t.day,t.hour,t.minute,t.second)
print(time.ctime())


