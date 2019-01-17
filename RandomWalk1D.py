# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:42:32 2019
"1D Random Walks"
@author: TRuTAn
"""
from random import random
import numpy as np
import matplotlib.pyplot as plt

#number of particles
N = 100
itrs = 1000000
x = np.zeros((itrs,N))
average = [0]

#function for movement
def move(temp):
    if random() <= 0.5:
        return temp + 1
    else: return temp -1

for i in range(1,itrs):
    for j in range(N):
        x[i][j] = move(x[i-1][j])
    average.append(sum(x[i])/N)
    
        
##plotting individual trajectories
#plt.plot(x[0])
    
#plotting average
plt.plot(average)
