lst = ["OK", "NOK", "hello", "hi"]
print(lst[-1], lst[-2], lst[0])
lst[-1] = "hello"
print(len(lst[1]))
print(lst[:2], lst[-2:])
print(lst[-1][::-1])
print(lst[1::2])
for i in lst:
    print(i)

for i in lst:
    print(len(i))