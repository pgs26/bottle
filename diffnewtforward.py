# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sympy as sp
'''n=int(input("Enter number of values:"))
x=[]
fx=[]

for i in range(n):
  x.append(float(input("Enter x:")))
  fx.append(float(input("Enter f(x):")))
'''
n=7
x=[3,4,5,6,7,8,9]
fx=[4.8,8.4,14.5,23.6,36.2,52.8,73.9]
table=[]
table.append(fx)

h=x[1]-x[0]
for i in range(n-1):
  t=[]
  for j in range(len(table[i])-1):
    t.append((table[i][j+1]-table[i][j])/(x[j+1+i]-x[j]))
  table.append(t)
b=[]
for i in range(len(table)):
  b.append(table[i][0])
def ch(n):
  if n>=0:
    return '+'
  else:
    return '-'
def fac(n):
    if n==1:
        return 1
    else:
        return (n*fac(n-1))
result=str(b[0])
value=b[0]

for i in range(1,n):
  result+=" %c %.2f"%(ch(b[i]),(b[i]))
  for j in range(i):
    result+="*(x %c %.2f)/%.2f"%(ch(-x[j]),abs(x[j]),fac(i))

polynomial=result
print(polynomial)

p=sp.symbols('x')
dydx=sp.Derivative(result,p).doit()
d2ydx2=sp.Derivative(result,p).doit()

X=input("\nEnter x for which the value of the function has to be found:")
dydx = str(dydx).replace("x",str((float(X)-x[0])/h))
print("\ndy/dx at %s = %.3f"%(X,eval(dydx)/h))

X=input("\nEnter x for which the value of the function has to be found:")
d2ydx2 = str(d2ydx2).replace("x",str((float(X)-x[0])/h))
print("\nd2y/dx2 at %s = %.3f"%(X,eval(d2ydx2)/h**2))    