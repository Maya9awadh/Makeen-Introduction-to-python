#import math library
import math

#initialize variable
b=15
r=100
n=2

#arthimetic operation 
exp=b*((1+r/100)**n)
print(exp)

exp2=b*1+r/100**n #without ()
print(exp2)

print((7*(10-5)%3)*4+9)
a=2
b=2
t=8

#use sqrt() and cos()
c=math.sqrt(a**2+b**2 - (2*a*b*math.cos(t)))
print(c)

#floor division
baisas=1729
omr=baisas//1000
baisas=baisas%1000 #remainder

print(omr, baisas)

#
price=4.35
quantity=100
total=price*quantity

print("%.2f" % total)#formate

x=434.999999
x=int(x*100)/100.0

x=ord("a")
print(x)