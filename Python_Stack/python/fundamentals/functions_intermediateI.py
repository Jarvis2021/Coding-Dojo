import random

def randInt(min=0, max=100):
    size = max - min
    num = random.random() * size + min
    return round(num)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
