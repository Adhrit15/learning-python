#Problem 11 
#Lets play games 
#1) ask user to guess a number from 1 to 100 
#not including 100 
#Then randomly guess a number in code from 1 to 100 
#if user number is less than code's number , then score is -1 
#if user number is equal to  code's number , then 3
#if user number is greater than code's number , then 1

#Play 10 times and sum of all scores, if it +, then user wins 
#if it is -ive, then code wins 
#Declare the winner 

#2) 
#ask user to guess a character from ABCD
#Ask user to guess a number from 1 to 13 including 13

#Code also guess a character from ABCD
#Code also guess  a number from  1 to 13 including 13

#if code's guess is greater or equal to than user, code wins 
#else user wins 

#Let user play in infinite loop 
#Use crtl+c to break 


#Example - 
#a)Code wins 
#User - A5 
#Code - A5,A6,..,B1,B2.....,C1,...D1,...

#b)Code wins 
#User - A13
#Code - Any combination 

#b)User wins 
#User - D13
#Code - Any combination except D13
import random
score = 0
for i in range(1, 11):
    print("Round", i)
    user = int(input("Guess a number from 1 to 99: "))
    computer = random.randint(1, 100)
    print("Computer's pick:", computer)
    if user < computer:
        score = -1
    elif user == computer:
        score = 3
    else:
        score = 1

    score += score
    print("current score:", score)
print("Final Score:", score)
if score > 0:
    print("Winner: User wins!")
else:
    print("Winner: Code wins!")
