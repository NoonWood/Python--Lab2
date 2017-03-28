# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:13:56 2017

@author: admin
"""

import argparse
import os
import shutil

def main():
    m = argparse.ArgumentParser(description = "Reorganize", epilog = "Mission complete!")
    m.add_argument("--source",type=str, default = '.',help = 'Destination')
    m.add_argument("--days",type=int, default = 2, help = 'How old are files? (days)')
    m.add_argument("--size",type=int,default = 1, help = 'Max size of files')
    options = m.parse_args()
    
    
    options = str(options)
    options = options[9:]
    options = options.replace('(','')
    options = options.replace(')','')
    options = options.replace(',','')
    listOptions = options.split(' ')
    print (listOptions)
    
    daysTo = listOptions[0]
    daysTo = daysTo.split('=')
    daysTo = daysTo[1]
    print(daysTo)                                                                       
    #Source
    source = listOptions[2]
    source = source.split('=')
    source = source[1]
    source = source.replace('\\\\','\\') #\\ na \
    source = source.replace('\'','')# ' na del
    print('Source',source)
    #Size
    size = listOptions[1]
    size = size.split('=')
    size = size[1]
    size = int(size)
    print(size)
 #Is it empty? if not i create folders there and sort files   
    if os.path.exists(source) == True:
        if os.listdir(source):
            #Some files
            #Create folders
            os.chdir(source)
            os.mkdir(str('Archive'))
            os.mkdir(str('Small'))
            
            files = os.listdir(source)
            files = [os.path.join(source, file) for file in files]
            files = [file for file in files if os.path.isfile(file)] #files only in list
            for i in range(len(files)):
                
                inseconds = daysTo * 2000
                inseconds = float(inseconds)
                print(files[i])
                #Move files
                if os.path.getmtime(files[i])>inseconds:
                    shutil.move(files[i],source+'\Archive')
                if os.path.getsize(files[i])<size:
                    shutil.move(files[i],source+'\Small')
        else:
            #No any files
            print('Directory is EMPTY!')
            print('YOU SHOULD INPUT CORRECT PATH!') 
     
#call func
if __name__ == '__main__':
    main()