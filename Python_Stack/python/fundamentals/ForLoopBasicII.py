# 1 . Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def convertbig(x):
    y = len(x)
    for val in range (0,y,1):
        if x[val] > 0:
            x[val] = 'big'
    return x

print(convertbig([-1,-3, 5, 6, -5, -9]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def count_positives(x):
    y = len(x)
    count = 0
    for i in range (0,y,1):
        if x[i] > 0:
            count = count + 1
    x[y-1] = count
    return x

print(count_positives([1,6,-4,-2,-7,-2]))



# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

def sumoflist(x):
    y = len(x)
    sum = 0
    for i in range(y):
        sum = sum + x[i]
    return sum

print(sumoflist([2,3,4,5,1]))

# Average - Create a function that takes a list and returns the average of all the values.

def averageoflist(x):
    y = len(x)
    sum = 0
    for i in range(y):
        sum = sum + x[i]
    avg = float(sum)/y
    return avg

print(averageoflist([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.


def lengthoflist(x):
    count = 0;
    y = len(x)
    for i in range(0,y,1):
        count = count + 1
    return count

print(lengthoflist([3,4,5,6,7,8]))



# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

def minimum(x):
    y = len(x)
    min = 0
    for i in range(0,y,1):
        if x[i] < min:
            min = x[i]
            return min
    else: return False

print(minimum([37,2,1,-9,-8]))
print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.


def maximum(x):
    y = len(x)
    max = 0
    for i in range(0,y,1):
        if x[i] > max:
            max = x[i]
            return max
    else: return False

print(maximum([37,2,1,-9,-8]))
print(maximum([]))



# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.


def createdictionary(x):
    dict = {}
    sum = 0
    min = 0
    y = len(x)
    for i in range (0,y,1):
        sum = sum + x[i]
     return sum
    for i in range (0,y,1):
        if x[i] < min:
            min = x[i]
    return min
    avg = float(sum)/y
