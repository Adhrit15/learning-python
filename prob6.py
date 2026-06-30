#PROBLEM Six 
#take a character to use for display from user 
#and till how many times, it will print 
#then print it 

#example , if display character is +
#and 5 times , then print below figure 
#+
#++
#+++
#++++
#+++++

char = input("enter character")
num = ("enter number of times")
n = int(num)
for i in range(n):
    for j in range(i+1):
        print("+")