#Problem One 
#lst = [1,2,3,5,6]
#Write below code 
#    1) how many elements 
#    2) is 7 part of lst 
#    3) compare with [1,2,3] if same , print "same" else "not-same"
#    4) add 10 to first element and update that value to first element 
lst = [1,2,3,4,5,6]
print(len(lst))
print(7 in lst)
if lst == [1, 2, 3]:
    print("same")
else:
    print("not-same")
lst[0] = lst[0] + 10
print(lst)