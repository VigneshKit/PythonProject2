import random

while True:
    num = random.randint(1,100)

    if num%2 == 0:
        continue
    print(num)
    if num == 1:
        break