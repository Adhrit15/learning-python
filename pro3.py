import random
numbers = [random.randint(10, 50) for i in range(10)]
total = sum(numbers)

print(f"List of random numbers: {numbers}")
print(f"Sum of the numbers: {total}")