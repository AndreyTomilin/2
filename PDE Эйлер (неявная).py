import numpy as np
import matplotlib.pyplot as plt

L = 10   #длина стержня
T = 100  #время расчета
a = 0.01 #коэффициент температуропроводности
N = 100  #число узлов пространственной сетки
K = 250  #число шагов по времени

def psi1(t): #ГУ слева (нулевая температура)
    return 25

def psi2(t): #ГУ справа (нулевая температура)
    return 25

def phi0(x): #Начальные условия 
    if (4.5 <= x <= 5.5): return 100
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

#заполняем матрицу коэффициентов левой части
A = np.zeros((N,N))
A[0,0] = 1
# A[0,1] = -Co/2
# A[N-1,N-2] = -Co/2
A[N-1,N-1] = 1
for i in range(1,N-1):
    for j in range (1,N-1):
        if i==j:
            A[i,j] = 1 + Co
            A[i,j-1] = -Co/2
            A[i,j+1] = -Co/2
print(A,u_new)
for k in range(1,K):
    u_old[0] = psi1(t[k])    #ГУ на концах стержня 
    u_old[N-1] = psi2(t[k])  #ГУ на концах стержня 
    u_new = np.linalg.solve(A,u_old)
    u_old[:] = u_new[:]

    if k == 15:
        plt.plot(x,u_new,'g-')
    if k == 100:
        plt.plot(x,u_new, 'b-')
    if k == 240:
        plt.plot(x,u_new, 'y-')
    
