# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:09:19 2017

@author: admin
"""

import re


#######
def searching(text):
    #text = text.lower
    for i in range(len(text)):
        pattern = re.compile(r'192.\d{0,3}.\d{0,3}.\d{0,3}')
        result = pattern.findall(text[i])
        searchForResult = pattern.search(text[i])
        if searchForResult != None:
            print('Строка ',i,' Позиция ',searchForResult.span(),' : ',result)
            

#######
def workWithFile(pathToFile):
    rfile = open(pathToFile)
    #fileString = rfile.read()
    fileString = rfile.readlines()   
    searching(fileString)
    

#######
finish_it = False
while finish_it !=True:
    try:
        _pathToFile = input('Введите путь к файлу (D:\Учеба\Python\git-lab1\Python-lab2\File for 4.txt)>> \n')
        workWithFile(_pathToFile)
        finish_it = True    
    except(FileNotFoundError,OSError):
        print('Файл не найден!')