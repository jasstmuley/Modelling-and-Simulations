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
itrs = 100
x = np.zeros((N,itrs))

##function for movement
#def move(temp):
#    if random() <= 0.5:
#        return temp + 1
#    else: return temp -1

for i in range(1,itrs):
    for j in range(N):
        if random() >= 0.5:
            x[j][i] = x[j][i-1] - 1
        else:
            x[j][i] = x[j][i-1] + 1
        
#plotting individual trajectories
plt.plot(x[0])
plt.plot(x[1])