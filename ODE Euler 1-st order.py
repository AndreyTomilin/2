# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

A = 2
t0 = 0
T = 2
N = 30
dt = (T-t0) / N

def f(t,y):
    return A*y
    
#рассчетна сетка по времени
t = []
y = [0]*(N+1)
for i in range(N+1):
    t.append(t0+i*dt)

#начальное приближение
y[0] = 1

#основной вычислительный цикл
for i in range(1,N+1):
    y[i] = y[i-1] + dt*f(t[i],y[i-1])

#результаты расчета
for i in range(1,N+1):
    print('t=',t[i],' ','y=',y[i])

t_anal = [t0+(T-t0)/100 *i for i in range(101)]
y_anal = [y[0]*exp(A*t) for t in t_anal]

plt.plot(t,y,'o',t_anal,y_anal,'-')