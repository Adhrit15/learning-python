input_str = "Hello world and Hello Earth"
words = input_str.split()
checked = []

for word in words:
    if word not in checked:
        count = 0
        for check in words:
            if word == check:
                count += 1
        print(f"{word} - {count}")
        checked.append(word)