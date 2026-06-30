input_str = "aaabbbbaaac"
unique_list = []
for char in input_str:
    if char not in unique_list:
        unique_list.append(char)
print(str(unique_list))