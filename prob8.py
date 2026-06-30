#PROBLEM eight  
#define a calculator for two complex number 
#calculator takes two complex numbers and ask for operations  

#Handles +, - , * , /   , sqrt, sin, cos, tan, log, exp
#prints the answer
#and again asks for two numbers 

#Use crtl+c to break 

#Hint:
#complex() as conversion, must not contain any space 
#Use str.replace(" ", "") to delete any space 
#Use while True for infinite loop
#use cmath
#PROBLEM seven 
#define a calculator for two float numbers 
#calculator takes two numbers and ask for operations  
#Handles +, - , * , /  , sqrt, sin, cos, tan, log, exp
#prints the answer
#Hints: use math 
#number is in radian
import cmath
num1_s = input("Enter first number")
num1_s = num1_s.replace(" ","")
num1 = complex(num1_s)

num2_s = input("Enter second number(enter 0 if not required)")
num2_s = num2_s.replace(" ","")
num2 = complex(num2_s)

operation = input("Enter operation")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "sqrt":
    print(cmath.sqrt(num1))
elif operation == "sin":
    print(cmath.sin(num1))
elif operation == "cos":
    print(cmath.cos(num1))
elif operation == "tan":
    print(cmath.tan(num1))
elif operation == "log":
    print(cmath.log(num1))
elif operation == "exp":
    print(cmath.e**num1)

else:
    print("invalid operation entered")
