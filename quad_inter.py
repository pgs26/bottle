import sympy as sp

x0,x1,x2,y0,y1,y2 = list(map(float,input("Enter the values of x0,x1,x2,f(x0),f(x1),f(x2)").split()))

b0 = y0
b1 = (y1-y0)/(x1-x0)
b2= (((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)

x = sp.Symbol('x')
exp = b0+b1*(x-x0)+b2*(x-x0)*(x-x1)
print("the expression is :",exp)

val = float(input("Enter the value of x :"))
res=exp.subs(x,val)
print("After substituting value of x :%0.2f"%(res))