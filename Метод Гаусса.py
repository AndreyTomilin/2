# -*- coding: utf-8 -*-

import numpy as np

n = 4
A = [[2,2,3,4],
     [5,6,7,8],
     [9,11,17,12],
     [13,14,15,19]
    ]
b = [1,2,3,4]
    
#прямой ход
#внешний цикл шаг преобразования Гаусса
for k in range(n-1):
    #цикл по строкам матрицы    
    for i in range(k+1,n):
        l = -A[i][k] / A[k][k]
        for j in range(k,n):
            A[i][j] = A[i][j] + l * A[k][j]
        b[i] = b[i] + l * b[k] 
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