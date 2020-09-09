from math import acos,pi,modf, degrees,cos
a,b,c=map(float,input().split())
"""if (a>=b and a>=c):"""
v=((b*b+c*c-a*a)/2*b*c)/(pi*2)
ugol=acos(v-int(v))
"""
degrees(ugol)
"""
bis=2*b*c*cos(ugol/2)/(b+c)
""""
if (b>=c and b>=a):
    ugol=acos((a*a+c*c-b*b)/2*a*c)
    bis=2*a*c*cos(ugol/2)/(a+c)
if (c>=a and c>=b):
    ugol=acos((a*a+b*b-c*c)/2*a*b) 
    bis=2*a*b*cos(ugol/2)/(a+b)
"""
print (bis)

