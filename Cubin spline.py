

import numpy as np
import sympy as sp

n=int(input("Enter number of values: "))
x=[]
fx=[]

for i in range(n):
  x.append(float(input("Enter x: ")))
  fx.append(float(input("Enter f(x): ")))

'''n=4
x=[1,2,3,4]
fx=[1,5,11,8]'''

h=x[1]-x[0]
d=[]
for i in range(1,n-1):
  d.append(6*(fx[i-1] - 2*fx[i] + fx[i+1])/(h*h))
a=np.zeros((n-2,n-2))
for i in range(n-2):
  for j in range(n-2):
    if i==j:
      a[i][j]=4
    elif abs(i-j)==1:
      a[i][j]=1

m=np.linalg.solve(a,np.array(d))
m=m.tolist()
m.insert(0,0)
m.insert(n,0)

px=[]
def ch(n):
  if n<0:
    return '-'
  else:
    return '+'


print("\nThe Cubic Equations:\n")
for i in range(n-1):
  t="%f*(%f - x)**3/6*%d %c %f*(x %c %f)**3/6*%d + (%f - x)*(%f %c %f*%d/6)/%d + (x %c %f)*(%f %c %f*%d/6)/%d"%(m[i],x[i+1],h,ch(m[i+1]),abs(m[i+1]),ch(-x[i]),abs(x[i]),h,x[i+1],fx[i],ch(-m[i]),abs(m[i]),h*h,h,ch(-x[i]),abs(x[i]),fx[i+1],ch(-m[i+1]),abs(m[i+1]),h*h,h)
  px.append(str(sp.expand(t)))
  print("p%d(x) = %s"%((i+1),px[i]))

X=float(input("\nEnter the x to find f(x):"))

for i in range(len(x)):
  if x[i] >= X:
    break

print("\nf(%.2f) = %.2f"%(X,eval((px[i-1]).replace('x',str(X)))))
