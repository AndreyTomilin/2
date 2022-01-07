# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#constants
sigma = 10.0
rho = 20
beta = 8.0/3.0

def lorenz(x, y, z):
    x_right = sigma*(y - x)
    y_right = (rho - z)*x - y
    z_right = x*y - beta*z
    return x_right, y_right, z_right

t0 = 0
T = 30
N = 10000
dt = (T-t0) / N

#рассчетна сетка по времени
t = []
for i in range(N+1):
    t.append(t0+i*dt)

#пустые массивы
x = [0]*(N+1)
y = [0]*(N+1)
z = [0]*(N+1)
   
#начальное приближение
x[0], y[0], z[0] = 1,2,3.000000001

for i in range(0,N):
    x_right, y_right, z_right = lorenz(x[i], y[i], z[i])
    x[i+1] = x[i] + dt*x_right
    y[i+1] = y[i] + dt*y_right  
    z[i+1] = z[i] + dt*z_right
fig1 = plt.figure(1)
ax1 = plt.axes()
ax1.plot(t,x)
fig2 = plt.figure(2) 		
ax2 = fig2.gca(projection='3d') 
ax2.plot(x,y,z)

