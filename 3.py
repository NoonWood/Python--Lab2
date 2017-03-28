# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:47:42 2017

@author: admin
"""

import os
import re
#import shutil
path = "D:\Учеба\Python\git-lab1\Python-lab2\Music"
#print(path)
basepath = os.path.abspath(os.path.dirname('Music'))
##print(basepath)
path = os.path.join(basepath, 'Music')
#----------------------------------------------
#Open txt, read-only, step-by-step
try:
    with open('Music\List.txt','r') as songList:
        formatedList = songList.readlines()
        dict = {}
except IOError as err:
    print(err)

for line in range(len(formatedList)):
    temp = formatedList[line]
    temp2 = formatedList[line]
    temp2 = str(temp2)
    temp2 = re.sub('\n',' ', temp2)
    #print(temp2)
    #temp = temp.split(' ')
    temp = re.sub('\n','',temp)
    dict[temp +'.mp3'] = str(temp2)
    
#temp = formatedList[2]
#temp = temp.split(' ') 

#print(temp)
#print(temp[1])
#print(dict)
list = []
for top, dirs, files in os.walk(path):
    for nm in files:
        fname =  os.path.join(top, nm)   
        fname = str(fname)#.encode('utf-8') 
        print('>>' + nm)
        list.append(fname)
    for i in range(len(formatedList)):
        formatedList[i]= formatedList[i]+'.mp3'
        print('To cto gde&&'+formatedList[i], dict.keys())
#        if formatedList[i] in dict.keys():
#            rtemp=formatedList[i]
#            os.renames(fname,top+"\\"+dict[rtemp]+'.mp3')
        #print( dict.keys())
#        if formatedList in dict.keys():
#            os.renames(fname,top+"\\"+dict[nm]+'.mp3')
#            #print(fname)
            #print('PATH TO MOVE ',top+"\\"+dict[nm]+'.mp3')
            #shutil.move('','')
#for i in range(len(formatedList)):
#    formatedList[i]= formatedList[i]+'.mp3'
#    print(formatedList[i], dict.keys())
#    
#    if formatedList[i] in dict.keys():
#        rtemp=formatedList[i]
#        os.renames(fname,top+"\\"+dict[rtemp]+'.mp3') 
#for i, filename in enumerate(os.listdir(basepath)):
#    os.chdir(basepath)
#    os.rename(filename, 'air{0}.png'.format(i+1))
