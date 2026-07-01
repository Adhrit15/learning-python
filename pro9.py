import random
scores = []
for i in range(10):
    print(f"Round {i + 1}")
    user_num = int(input("Guess a number from 1 to 99: "))
    code_num = random.randint(1, 99)
    print(f"Code picked: {code_num}")
    if user_num < code_num:
        scores.append(-1)
        print("Result: You guessed lower. Score: -1")
    elif user_num == code_num:
        scores.append(3)
        print("Result: Exact match! Score: 3")
    elif user_num > code_num:
        scores.append(1)
        print("Result: You guessed higher. Score: 1")
total_score = sum(scores)
print(f"Total Score: {total_score}")

if total_score > 0:
    print("You win!")
elif total_score < 0:
    print("Code wins!")
else:
    print("It's a tie!")