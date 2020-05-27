'''
input : log-file
output: print if device rebooted 
'''

import copy
import re
import datetime
import configuration as conf


import matplotlib.dates as md
import matplotlib.pyplot as plt
from datetime import datetime
import math
import time


def uptime(fname):
    #open and read lines from log-file
    infile=open(fname,"r")
    lines=infile.readlines()
    upout=open("uptime.txt","w+")
    v = False

    for line in lines:
        line=line.strip()
        if conf.device_prompt+" uptime" in line:
            v=True
        elif conf.device_prompt+" free" in line:
            v=False
        elif v:
            upout.write(line+"\n")

    upout.close()
    upout=open("uptime.txt","r")
    upl=upout.readlines()

    tmp=[]

    uptemp=open("uptime.txt","r")
    uplt=uptemp.readlines()
    for i in uplt:
        j=i.find("load")
        tmp.append(i[12:j-3])

    tmp3=[]
    
    #convert the sliced value of uptime into integer and reduce it into seconds
    for i in tmp:
        if "min" in i and ":" not in i and "day" not in i :
            m=i[0:2]
            tmp3.append(int(m)*60)
        elif ":" in i and "day" not in i and "min" not in i:
            h, m = i.split(':')
            tmp3.append(int(h) * 3600 + int(m)*60)
        elif "day" in i and "min" in i:
            tmp3.append(int(i[0])*24*3600+int(i[7:9])*60 )
        elif "day"  in i and ":" in i:
            d=int(i[0])
            m,s=int(i[7:9]),int(i[10:12])
            tmp3.append(d*24*3600+m*3600+s*60 )
    tmp2=copy.deepcopy(tmp3)  
    tmp2.sort()
    c=0
    #compare if items in orginal list(containing seconds) to get number of restarts
    for i in range(1,len(tmp3)-1):
        if tmp3[i]<tmp3[i+1]:
           continue
        else:
            c=c+1
    print("number of reboots : ",c)
    if len(tmp2) !=0 and len(tmp3) != 0:
        
        if tmp2==tmp3:
            print("No problem in uptime")
        else:
            print(" Device has rebooted   ")
    else:
        print("error !!! either value assigned to logfile or device_prompt is incorrect \n")
    infile.close()





