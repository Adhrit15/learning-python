#PROBLEM one 
#define a calculator for two float numbers 
#calculator takes two numbers and ask for operations  

#Handles +, - , * and /  
#prints the answer
num1_s = input("Enter first number")
num1 = float(num1_s)
num2_s = input("Enter second number")
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
else:
    print("invalid operation entered")
