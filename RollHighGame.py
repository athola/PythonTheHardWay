import random

truetotal = 0
putIn = (125)
for j in range(0, 50):
    total = 0
    for i in range(0, 10000):
        i = random.randint(0, 10000);
        if i == 8888:
            total += 1000000
        total -= 125
    print(total)
    truetotal += total
print(truetotal/50)

    
    
