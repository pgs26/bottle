a=[]
y=[]

n=int(input("Enter the order n :"))

for i in range(n):
    temp=float(input("Enter the values of y"+str(i)+" :" ))
    a.append(temp)
    temp=float(input("Enter the values of f(y"+str(i)+") :"))
    y.append(temp)
yp=0
pt=float(input("Enter the value of y to substitute:"))
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (pt - y[j])/(y[i] - y[j])
    yp = yp +p* a[i] 

print("the value of x is :",yp)
