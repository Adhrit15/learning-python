#PROBLEM five  
#define a calculator for two complex number 
#calculator takes two complex numbers and ask for operations  

#Handles +, - , * and /  
#prints the answer
#and again asks for two numbers 

#Use crtl+c to break 

#Hint:
#complex() as conversion, must not contain any space 
#Use str.replace(" ", "") to delete any space 
#Use while True for infinite loop
while True:
    num1_s = input("Enter first number")
    num1 = num1_s.replace(" ","")
    num2_s = input("Enter second number")
    num2 = num2_s.replace(" " ,"")
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
