# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

A = 2
t0 = 0
T = 3
N = 20
dt = (T-t0) / N

def f(t,y):
    return A*y
    
#рассчетна сетка по времени
t = []
y = [0]*(N+1)
y_second = [0]*(N+1)
y_forth = [0]*(N+1)
for i in range(N+1):
    t.append(t0+i*dt)

#1-го порядка
#начальное приближение
y[0] = 1
for i in range(0,N):
    y[i+1] = y[i] + dt*f(t[i],y[i])

#2-го порядка
#начальное приближение
y_second[0] = 1
for i in range(0,N):
    y_tilda = y_second[i] + dt*f(t[i],y_second[i])
    y_second[i+1] = y_second[i] + dt/2 * (f(t[i],y_second[i]) + f(t[i+1],y_tilda))
    
#4-го порядка
#начальное приближение
y_forth[0] = 1
for i in range(0,N):
    k1 = f(t[i],y_forth[i])
    k2 = f(t[i]+dt/2,y_forth[i]+dt/2*k1)
    k3 = f(t[i]+dt/2,y_forth[i]+dt/2*k2)
    k4 = f(t[i]+dt,y_forth[i]+dt*k3)
    y_forth[i+1] = y_forth[i] + dt/6*(k1+2*k2+2*k3+k4)

t_anal = [t0+(T-t0)/100 *i for i in range(101)]
y_anal = [y[0]*exp(A*t) for t in t_anal]

plt.plot(t_anal,y_anal,'-', t,y,'o',t,y_second,'x',t,y_forth,'D')
