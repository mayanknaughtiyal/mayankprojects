#pythont progrrame to find roots of a quadratic eauation
#d=b^2-4ac
|#x=(-b+-d^1/2)/2a
import cmath
a= float(input("enter the cofficient a"))
b= float(input("enter the cofficient b"))
c= float(input("enter THE COFFICIENT c"))
d=b**2-4*a*c
root1=(-b+cmath.sqrt(d))/2*a
root2=(-b-cmath.sqrt(d))/2*a
print("roots of the quadratic equation are"root1,root2)
