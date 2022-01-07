# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

N = 25

x = np.linspace(0,1,N)
y = np.linspace(0,1,N)

u_old = np.zeros((N,N))
u_new = np.zeros((N,N))

#ГУ по периметру прямоугольника
u_new[0,:] = 10     #нижняя граница
u_new[N-1,:] = 30   #верхняя граница
u_new[:,0] = 20     #левая граница
u_new[:,N-1] = 40   #правая граница

delta = np.inf
eps = 0.01

while (delta > eps):
    for i in range(1,N-1):
        for j in range (1,N-1):
            u_new[i,j] = 1/4 * (u_old[i+1,j] + u_old[i-1,j] + u_old[i,j+1] + u_old[i,j-1])
    
    delta = np.max(np.abs(u_new - u_old))
    u_old[:] = u_new[:]
 
X, Y = np.meshgrid(x, y) 	
plt.contourf(X, Y, u_new, cmap=plt.cm.rainbow)


