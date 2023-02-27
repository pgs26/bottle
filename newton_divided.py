import sympy as sp
a=[]
y=[]

n=int(input("Enter the order n :"))

for i in range(n):
    temp=float(input("Enter the values of x"+str(i)+" :" ))
    a.append(temp)
    temp=float(input("Enter the values of f(x"+str(i)+") :"))
    y.append(temp)
   

fin_ans=[]
fin_ans.append(y[0])
j=n
for i in range(n-1):
    temp=[]
    for z in range(j-1):
        diff=(y[z+1]-y[z])/(a[i+z+1]-a[z])
        temp.append(diff)
    if(temp!=[]):
        fin_ans.append(temp[0])
    y=temp
    j-=1

res=fin_ans[0]
x=sp.Symbol('x')
m=1
for i in range(1,n):
    m*=(x-a[i-1])
    res+=(m*fin_ans[i])

print(res)