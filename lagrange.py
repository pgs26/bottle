import sympy as sp
a=[]
y=[]

n=int(input("Enter the order n :"))

for i in range(n):
    temp=float(input("Enter the values of x"+str(i)+" :" ))
    a.append(temp)
    temp=float(input("Enter the values of f(x"+str(i)+") :"))
    y.append(temp)

yp=0
pt=float(input("Enter the value of x to substitute:"))
x=sp.Symbol('x')
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (x - a[j])/(a[i] - a[j])
    
    yp = yp + p * y[i] 

print("the interpolated expression is :",yp)

print("The interpolated value is :",yp.subs(x,pt))