
# coding: utf-8

# In[1]:

#This script is used to plot the band above the CBM
import numpy as np
import sys, os, math
import matplotlib.pyplot as plt 
from scipy.interpolate import spline
from matplotlib.pyplot import cm
from matplotlib import style
plt.switch_backend('agg') 

# In[2]:

###Read E-Fermi from OUTCAR
fermiline=os.popen('grep "E-fermi" OUTCAR').readline()
Efermi=float(fermiline.strip().split()[2])
print Efermi


# In[3]:

###Read data from EIGENVAL file, to get the energy level of each band corresponding to each k-point
###This file can be get from DOS calculation
eigfile=open('EIGENVAL','r')
data=eigfile.readlines()
NK=data[5].split()[1]
NB=data[5].split()[2]
band=[]
#print NK
#print len(data)
for i in range(7,len(data)):
    if data[i] != '\n':
        band.append(data[i].strip().split())


# In[4]:

energy=[]
n=0
for i in range(0,len(band)):
    if len(band[i])==3:
        if int(band[i][0])>=429 and int(band[i][0])<=445 :  #Determine the band number range, can be changed 
            n=n+1
            energy.append(band[i][1])
        else: 
             pass
    else: 
        pass


# In[5]:

interval=(445-429+1) 
kp=n/interval
#print kp
kpoint=[]
for i in range(0,kp):
    kpoint.append(i)
level=[[kk for kk in range(0,kp)] for nn in range(0,interval)]

for i in range(0,kp):
    for j in range(0,interval):
        level[j][i]=float(energy[i*interval+j])-Efermi


# In[6]:
print level[0][0]
print level[5][0]
print level[9][0]
#print level[5][0]


# In[7]:

style.use('seaborn-poster')


# In[8]:

colors=['g','g','g','g','g','r','c','y','b','k','r','m','m','m','m','m','m'] 
width=['1','1','1','1','1','4','1','1','1','3','1','1','1','1','1','1','1'] 
for i in range(0,interval): 
    plt.plot(kpoint,level[i],'-o',color=colors[i],linewidth=width[i],label="band%d"%i) 
    #plt.plot(kpoint, level[i],'-o',linewidth=2,label="band%d"%i)
    plt.legend(loc=1,fontsize='small') 
    plt.xlim(0,30)

plt.savefig('comp-2.5-IP-band.png', dpi=300)

