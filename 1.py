# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:40:23 2017

@author: admin
"""
try:
    with open(r'File for 1.txt', 'rt') as f:
        lines = (str(f.read())).lower()
#       lines.strip()
        #print(lines)
except IOError as err:
    print(err)

mass=[]
for i in range(len(lines)):
    if lines[i].isalpha():#only letters
        mass.append(lines[i])

This={}
for i in range(len(mass)):
    num=0
    for j in mass:
        if mass[i]==j:
            num = num+1
            This[mass[i]]=num
            #mass[i]={mass[i], num}
                    
lam = lambda x: x[1]
Sorted = sorted(This.items(), key=lam, reverse=True) 
print ('Sorted:', Sorted)
f.close()
