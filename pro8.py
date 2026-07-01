total = []

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            if x*x + y*y == z*z:
                total.append(sum([x, y, z]))

print(f"{total}")