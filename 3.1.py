import math

a=eval(input("a="))
b=eval(input("b="))
c=eval(input("c="))
p=b*b-4*a*c
if p>0:
    x1=(-b+math.sqrt(p))/(2*a)
    x2=(-b-math.sqrt(p))/(2*a)
    print("x1={:.2f}".format(x1) )
    print("x2={:.2f}".format(x2) )
else:
    print("方程没有实数根")