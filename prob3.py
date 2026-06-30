#PROBLEM Three 
#Print prime numbers between 0 to 100

#Hint:
#prime number is a number which can not be divided 
#by any number except 1 and that number 
#Use % to see the remainder is 0, then it is perfect divisible 
print("2")
i = 3
while i < 101:
    upper_bound = int(i**0.5) +1
    for j in range(3,upper_bound,2):
        if i % j == 0:
            break
    else:
        print(i)
    i+=2
    