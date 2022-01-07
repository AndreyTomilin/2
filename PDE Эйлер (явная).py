
import numpy as np
import matplotlib.pyplot as plt

L = 1   #длина стержня
T = 100  #время расчета
a = 0.0001 #коэффициент температуропроводности
N = 100  #число узлов пространственной сетки
K = 250  #число шагов по времени

def psi1(t): #ГУ слева (нулевая температура)
    return 25

def psi2(t): #ГУ справа (нулевая температура)
    return 25

def phi0(x): #Начальные условия 
    if (0.45 <= x <= 0.55): return 100
    else: return 25

x = np.linspace(0,L,N)  #пространственная сетка
t = np.linspace(0,T,K)  #временная сетка
dx = x[1] - x[0]        #шаг пространственной сетки
dt = t[1] - t[0]        #шаг временной сетки
Co = 2*dt*a/dx**2       #число Куранта
print('Co=',Co)

u_old = [phi0(el) for el in x]
u_new = np.zeros(N)
plt.plot(x,u_old,'r-')
for k in range(1,K): #цикл по времени
    u_new[0] = psi1(t[k])    #ГУ на концах стержня 
    u_new[N-1] = psi2(t[k])  #ГУ на концах стержня 
    for i in range(1,N-1):
        u_new[i] = Co/2 * u_old[i-1] + (1-Co) * u_old[i] + Co/2 * u_old[i+1]
    u_old[:] = u_new[:]


    if k == 25:
            plt.plot(x,u_new,'g-')
    if k == 100:
            plt.plot(x,u_new, 'b-')
    if k == 240:
            plt.plot(x,u_new, 'y-')
