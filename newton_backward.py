import math
x=[]
n=int(input("Enter the order n :"))

y=[[0.0 for i in range(n)]for j in range(n)]
for i in range(n):
    x.append(float(input("Enter the values of x"+str(i)+" :" )))

for i in range(n):
    y[i][0]=float(input("Enter the values of y"+str(i)+" :"))

pt=float(input("Enter the point of interpolation :"))
#calculating the forward difference
for i in range(1,n):
    for j in range(n-1,i-1,-1):
        y[j][i]=y[j][i-1]-y[j-1][i-1]

#print the table
for i in range(n):
    for j in range(i+1):
        print(y[i][j],end="\t")
    print()

res=y[n-1][0]

u=(pt-x[n-1])/(x[1]-x[0])

for i in range(1,n):
    temp=u
    for j in range(i):
        temp=temp*(u+j)
    res=res+(temp*y[n-1][i])/math.factorial(i)

print("the interpolated value at %0.0f is %0.2f"%(pt,res))