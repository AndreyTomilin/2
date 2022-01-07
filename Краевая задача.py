import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# y'' + y'/x +2y = x, y(0.7)=0.5, y'(2)=-1.2
#Преобразуем уравнение к ситеме:
#y' = y1
#y1' = x - 2*y - y1/x

N = 20
a, b = 0.7, 2
y_a = 0.5
dy_b = -1.2 #задается производная на правой границе

def D(x, y):
    #y[0] - сама функция y(x)
    #y[1] - производная y'(x)
    return y[1], x-2*y[0]-y[1]/x


def bc(ya, yb):
    return ya[0] - y_a, yb[1] - dy_b

x = np.linspace(a, b, N)
y = np.zeros( (2, N) )  #2 - количество уравнений в системе


res = solve_bvp(D, bc, x, y)
x_plot = np.linspace(a, b, 100)
y_plot = res.sol(x_plot)[0]
plt.plot(x_plot, y_plot, label='y(x)')


#Метод конечных разностей
M = np.zeros((N,N))
A = np.zeros(N)
B = np.zeros(N)
C = np.zeros(N)
f = np.zeros(N)
h = x[1] - x[0]
for i in range(0,N-1):
    A[i] = 1/h**2 - 1/x[i]/(2*h)
    B[i] = 2 - 2/h**2
    C[i] = 1/h**2 + 1/x[i]/(2*h)
    f[i] = x[i]
k1 = 1
k2 = 0
k3 = 0
k4 = 1
B0 = k1 - k2/h
C0 = k2/h
Bn = k3 + k4/h
An = -k4/h
f[0] = y_a
f[N-1] = dy_b
M[0,0] = B0
M[0,1] = C0
M[N-1,N-1] = Bn
M[N-1,N-2] = An
for i in range(1,N-1):
    for j in range(N):
        if i == j:
            M[i,i-1] = A[i]
            M[i,i] = B[i]
            M[i,i+1] = C[i]
print(M)
y = np.linalg.solve(M,f)
plt.plot(x,y,'o')            