#!/usr/bin/python
# coding=utf-8
import json

__author__ = 'qishuhua'
controllist = ['1', '0']
controltype = controllist[0]
text = lambda controltype: 'Start' if controltype == '1' else 'Stop'
print(text(controllist[1]))

str ='1, 2, 3, 4'
list = str.split(',')
Filelist = []
for i in list:
    dict={}
    dict['FileNumber'] = int(i)
    Filelist.append(dict)
filedict={}
filedict['VoiceFileList'] = Filelist
print(json.dumps(filedict))

ddd='1,2,3'
for i in ddd.split(','):
    print(i)
