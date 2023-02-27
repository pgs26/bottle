import sympy as sp

x0,x1,fx0,fx1=list(map(float,input("Enter x0,x1,fx0,fx1 :").split()))

x=sp.Symbol('x')

y=fx0+((fx1-fx0)/(x1-x0))*(x-x0)

print("the linear equation is :",y)

temp=float(input("Enter the x value :"))

res=y.subs(x,temp)

print("After substituting value of x :%0.2f"%(res))