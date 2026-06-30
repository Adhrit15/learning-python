#PROBLEM Four 
#Print Pythogorus number  below 100
#ie (x,y,z) which satisfy z*z == x*x +y*y 
import math
c = 1
for a in range(1,100,1):
    for b in range(1,100,1):
        if c <= 100:
            c = (a * a) + (b * b)
            c = math.sqrt(c)
            if c % 1 == 0:
                print(c,b,a)
    
    

        