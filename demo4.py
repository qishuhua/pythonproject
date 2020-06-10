# import fcntl
# import socket
# import struct
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP = socket.inet_ntoa(fcntl.ioctl(

#         s.fileno(),

#         0x8915,  # SIOCGIFADDR

#         struct.pack('24s','edge0')

# )[20:24])
# print(IP)
import datetime
print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))