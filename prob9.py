#Problem nine 
#Lets solve some physics questions 
#https://en.wikipedia.org/wiki/Kinematics_equations#Kinematic_equations_for_linear_motion
#1) Take u, a, t from users and find final velocity v 
#2)Take u, a, s and find final velocity
#3)Take u,t,a and find s 
#where 
#initial velocity = u 
#final velocity = v 
#time after = t 
#distance moved = s 

print("1. Find final velocity (v) using u, a, t")
print("2. Find final velocity (v) using u, a, s")
print("3. Find distance moved (s) using u, t, a")
choice = input("Enter your choice (1, 2, 3): ")
if choice == "1":
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    t = float(input("Enter time (t): "))
    v = u + (a * t)
    print(v)
if choice == "2":
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    s = float(input("Enter distance (s): "))
    v' = (u ** 2) + (2 * a * s)
    v = v' ** 0.5
    print(v)
if choice == "3":
    u = float(input("Enter initial velocity (u): "))
    t = float(input("Enter time (t): "))
    a = float(input("Enter acceleration (a): "))
    s = (u * t) + (0.5 * a * (t ** 2))
    print(s)
