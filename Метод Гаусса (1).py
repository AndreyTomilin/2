# -*- coding: utf-8 -*-

import numpy as np

n = 4
A = [[2,1,-0.1,1],
     [0.4,0.5,4,-8.5],
     [0.3,-1,1,5.2],
     [1,0.2,2.5,-1.0]
    ]
b = [1,2,3,4]
    
#прямой ход
#внешний цикл шаг преобразования Гаусса
for k in range(n-1):
    #главный элемент первой строки к-го шага
    Major = A[k][k]
    #цикл по строкам матрицы    
    for i in range(k,n):
        for j in range(k,n):
            if (i == k):
                A[k][j] = A[k][j] / Major
            else:
                A[i][j] = A[i][j] - A[i][k] * A[k][j]
    b[i] = b[i] - A[i][k] * b[k] 
print(A)

#обратный ход
x = [0] *n
x[n-1] = b[n-1] / A[n-1][n-1]
for i in range(n-2,-1,-1):
    S = 0
    for j in range(i+1,n):
        S = S + A[i][j]*x[j]
    x[i] = (b[i]-S) / A[i][i]
print(x)

print(np.linalg.solve(A,b) )