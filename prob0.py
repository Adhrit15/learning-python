#Problem zero 
#From 0 to 100, print fizz if even number 
#and print fuzz if odd number 
#sleep 1 sec in between 

#Hint- for sleep, we need to use time module

import time
i=0
while i <= 100:
    if i % 2 == 0:
        print("fizz")
    else:
        print("fuzz")
    i+=1
    time.sleep(1)
    
    


