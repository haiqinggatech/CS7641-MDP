# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:57:10 2017

@author: Jon
"""

import pickle as pkl
import matplotlib.pyplot as plt
import numpy as np

def plotMap(name):
  name = '../../results/' + name
  with open(name,'rb') as f:
      arr = pkl.load(f, encoding='latin1')

  lookup = {'None': (0,0),
            '>': (1,0),
          'v': (0,-1),
          '^':(0,1),
          '<':(-1,0)}    

  n= len(arr)
  arr = np.array(arr)    
  X, Y = np.meshgrid(range(1,n+1), range(1,n+1))    
  U = X.copy()
  V = Y.copy()
  for i in range(n):
      for j in range(n):
          U[i,j]=lookup[arr[n-i-1,j]][0]
          V[i,j]=lookup[arr[n-i-1,j]][1]

  plt.figure()
  #plt.title('Arrows scale with plot width, not view')
  Q = plt.quiver(X, Y, U, V,headaxislength=5,pivot='mid',angles='xy', scale_units='xy', scale=1)
  plt.xlim((0,n+1))
  plt.ylim((0,n+1))
  plt.tight_layout()
  plt.show()

plotMap('easy/maps/Policy Easy Iter 30 Policy Map.pkl')
plotMap('hard/maps/Policy Hard Iter 22 Policy Map.pkl')