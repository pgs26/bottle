import math as m
from sympy import var
from sympy import sympify
 
def simpsons_1by3( lower_limit, upper_limit, n ,f): 
    h = ( upper_limit - lower_limit )/n
    xb = list()
    fx = list()
    i = 0
    while i<= n:
        xb.append(lower_limit + i * h)
        fx.append(f.subs(x,xb[i]))
        i += 1
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res

def simpsons_3by8(lower_limit, upper_limit, interval_limit,f ):    
    h = (float(upper_limit - lower_limit) / interval_limit)
    sum = f.subs(x,lower_limit) + f.subs(x,upper_limit)
    for i in range(1, interval_limit ):
        if (i % 3 == 0):
            sum = sum + 2 * f.subs(x,lower_limit + i * h)
        else:
            sum = sum + 3 * f.subs(x,lower_limit + i * h)
     
    return ((float( 3 * h) / 8 ) * sum )     

def trapezoidal(lower_limit,upper_limit,n,f):
    h = (upper_limit - lower_limit) / n
    
    integration = f.subs(x,lower_limit) + f.subs(x,upper_limit)
    
    for i in range(1,n):
        k = lower_limit + i*h
        integration = integration + 2 * f.subs(x,k)
    
    integration = integration * h/2
    
    return integration


eq = input("Enter equation f(x):")
lower_limit = float(input("Enter the lower limit : "))
upper_limit = float(input("Enter the upper limit : "))

x = var('x')
f = sympify(eq)

n = 6 
#f = lambda x :eval(eq)
print(f)
print("The value of the given integral using Simpsion's 1/3 rule : ",simpsons_1by3(lower_limit, upper_limit, n,f))
print("The value of the given integral using Simpsion's 3/8 rule : ",simpsons_3by8(lower_limit, upper_limit, n,f))
print("The value of the given integral using trapezoidal rule : ",trapezoidal(lower_limit, upper_limit, n,f))






