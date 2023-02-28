import numpy as np
import sympy as syp
import math
n=int(input("Enter the no of terms:"))
x=[float(input("Enter the value of x"+str(i)+" : " )) for i in range(n)]
table=np.zeros((n,n))
table[:,0]=[float(input("Enter the value of y"+str(i)+" : " )) for i in range(n)]
x_val=float(input("Enter the value of x:"))
for j in range(1,n):
    for i in range(j,n):
        table[i][j]=table[i][j-1]-table[i-1][j-1]
res=0
index=1
table=table[1:,:]
h=x[1]-x[0]
x1=syp.Symbol('x')
p=(x1-x[index])/h
for i in range(n-1):
    temp=table[i][i]
    for j in range(i):
        temp=temp*(p-j)
    temp=temp/math.factorial(i)
    res+=temp
    
eqn=syp.diff(res,x1)
print("First order Newton Forward ",eqn.subs(x1,x_val))
eqn=syp.diff(eqn,x1)
print("Second order Newton Forward ",eqn.subs(x1,x_val))    
