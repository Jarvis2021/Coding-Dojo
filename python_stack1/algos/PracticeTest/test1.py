# Multiples
# Part 1 Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for i in range(0,1000):
    if i%2!=0:
        print (i)

#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for i in range(5,1000001):
    if i%5==0:
        print(i)
    else:
        continue


# SumList - Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

x =  [1, 2, 5, 10, 255, 3]

def sumList(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum

print(sumList(x))

# Average List

def AvgList(x):
    sum = 0
    for i in x:
        sum = sum + i
        avg = sum/2;
    return avg

print(AvgList(x))
