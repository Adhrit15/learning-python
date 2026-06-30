#Problem ten 
#Lets do some linear algebra 
#(** means power in python)
#1) prove that (a+b)** 2 = a**2 + 2*a*b + b**2
#2) Similarly prove for (a+b)**3, (a+b)**4

#Hint 
#Take a and b and power from user , power can be 2,3,4
#https://en.wikipedia.org/wiki/Binomial_theorem
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
LHS = (a + b) ** 2
RHS = (a ** 2) + (2 * a * b) + (b ** 2)
print("Left Side ( (a+b)**2 )   =", LHS)
print("Right Side (Expanded)     =", RHS)
print("LHS=RHS, HENCE PROVED")


LHS = (a + b) ** 3
RHS = (a ** 3) + (3 * (a ** 2) * b) + (3 * a * (b ** 2)) + (b ** 3)
    
print("Left Side ( (a+b)**3 )   =", LHS)
print("Right Side (Expanded)     =", RHS)
print("LHS=RHS, HENCE PROVED")
LHS = (a + b) ** 4
RHS = (a ** 4) + (4 * (a ** 3) * b) + (6 * (a ** 2) * (b ** 2)) + (4 * a * (b ** 3)) + (b ** 4)
    
print("Left Side ( (a+b)**4 )   =", LHS)
print("Right Side (Expanded)     =", RHS)
print("LHS=RHS, HENCE PROVED")

