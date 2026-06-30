#PROBLEM seven 
#define a calculator for two float numbers 
#calculator takes two numbers and ask for operations  
#Handles +, - , * , /  , sqrt, sin, cos, tan, log, exp
#prints the answer
#Hints: use math 
#number is in radian
import math
num1_s = input("Enter first number")
num1 = float(num1_s)
num2_s = input("Enter second number(enter 0 if not required)")
num2 = float(num2_s)
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
    print(math.sqrt(num1))
elif operation == "sin":
    print(math.sin(num1))
elif operation == "cos":
    print(math.cos(num1))
elif operation == "tan":
    print(math.tan(num1))
elif operation == "log":
    print(math.log(num1))
elif operation == "exp":
    print(math.e**num1)

else:
    print("invalid operation entered")