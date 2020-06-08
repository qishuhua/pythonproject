# /usr/bin/python
# coding=utf-8
import os

FILE_PATH = 'd:\\datacenter\\campic2\\'
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)

print "os.path.dirname(__file__):", os.path.dirname(__file__)
print os.path.abspath(os.path.dirname(__file__))

if os.path.exists('d:\\datacenter\\campic\\'):
    files = os.listdir('d:\\datacenter\\campic\\')
    print files
    for i in range(len(files)):
        print os.path.abspath(os.path.dirname(files[i]))
        if os.path.isdir('d:\\datacenter\\campic\\' + files[i]):
            print "dir", files[i]
        elif os.path.isfile('d:\\datacenter\\campic\\' + files[i]):
            print 'filename', files[i]
