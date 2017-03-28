# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:08:27 2017

@author: admin
"""

import os
import re

path = "D:\Учеба\Python\git-lab1\Python-lab2\Music"
#print(path)
basepath = os.path.abspath(os.path.dirname('Music'))
path = os.path.join(basepath, 'Music')
#----------------------------------------------

songList = open('Music\List.txt','r')
formatedList = songList.readlines()
dict = {}
    
for line in range(len(formatedList)):
    temp = formatedList[line]
    temp2 = formatedList[line]
    temp2 = str(temp2)
    temp2 = re.sub('\n',' ', temp2)
    print('temp2  ' + temp2)
    temp = temp.split(' ')
    dict[temp[1]+'.mp3'] = str(temp2)

for top, dirs, files in os.walk(path):
    for nm in files:
        fname =  os.path.join(top, nm)   
        fname = str(fname)#.encode('utf-8') 
        print(' nm ' + nm)
        print('DICT.KEYS  ',dict.keys())
        if nm in dict.keys():
            os.rename(fname,top+"\\"+dict[nm]+'.mp3')