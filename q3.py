def trapezoidal(h,sub_int,v):
    res=v[0]+v[len(v)-1]

    for i in range(1,sub_int):
        res=res+2*v[i]
    res=res*h/2
    return res

def simpson13(h,sub_int,v):
    res=v[0]+v[len(v)-1]

    for i in range(1,sub_int):
        if i%2==0:
            res=res+2*v[i]
        else:
            res=res+4*v[i]
    res=res*h/3

    return res

def simpson38(h,sub_int,v):
    res=v[0]+v[len(v)-1]

    for i in range(1,sub_int):
        if i%3==0:
            res=res+2*v[i]
        else:
            res=res+3*v[i]
    res=res*3*h/8
    return res    
lower=0
upper=40
sub_int=9
v=[30,24,19.5,16,13.6,11.7,10,8.5,7]
h=5
res1=trapezoidal(h,sub_int,v)
res2=simpson13(h,sub_int,v)
res3=simpson38(h,sub_int,v)
print("The resulf of trapezoidal method :",res1)
print("The resulf of simpson 1/3 rule method :",res2)
print("The resulf of simpson 3/8 method :",res3)
