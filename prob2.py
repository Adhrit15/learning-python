#if name is "XYZ" and age is below 40, 
#print "suitable" else if age is greater
#than 50, print "old", else print "OK"
#For all other names, print "not known"

name = "XYZ"
age = 38
if name == "XYZ":
    if age < 40:
        print("suitable")
    elif age > 50:
        print("old")
    else:
        print("OK")
else:
    print("not known")


