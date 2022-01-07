
import numpy as np
import matplotlib.pyplot as plt

L = 1   #длина стержня
T = 100  #время расчета
a = 0.2 #коэффициент натяжения струны
N = 50  #число узлов пространственной сетки
K = 2000  #число шагов по времени

def psi1(t): #ГУ слева (концы закреплены)
    return 0

def psi2(t): #ГУ справа (концы закреплены)
    return 0

def phi(x): #Начальное положение струны 
    return np.sin(x/L * np.pi)

def v(x): #Начальная скорость струны 
    return -np.sin(x/L * np.pi)

x = np.linspace(0,L,N)  #пространственная сетка
t = np.linspace(0,T,K)  #временная сетка
dx = x[1] - x[0]        #шаг пространственной сетки
dt = t[1] - t[0]        #шаг временной сетки
Lambda = a**2 * dt**2 / dx**2
print('Lambda=',Lambda)

u_old = [phi(el) for el in x]
u_curr = [phi(el) + dt*v(el) for el in x]
u_new = np.zeros(N)
plt.plot(x,u_old,'r-')
for k in range(1,K): #цикл по времени
     u_new[0] = psi1(t[k])    #ГУ на концах стержня 
     u_new[N-1] = psi2(t[k])  #ГУ на концах стержня 
     for i in range(1,N-1):
         u_new[i] = 2*(1-Lambda) * u_curr[i] + Lambda * (u_curr[i+1] + u_curr[i-1]) - u_old[i]
     u_old[:] = u_curr[:]
     u_curr[:] = u_new[:]

     if k == 5:
           plt.plot(x,u_new,'g-x')
     if k == 10:
           plt.plot(x,u_new, 'b-o')
     if k == 80:
           plt.plot(x,u_new, 'y-')
     if k == 100:
           plt.plot(x,u_new, 'm-')
