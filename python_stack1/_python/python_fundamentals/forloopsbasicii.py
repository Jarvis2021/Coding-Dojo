# Biggie Size Given a list, write a function that changes all positive numbers in the list to "big".

# def convertbig(x):
#     y = len(x)
#     for i in range(y):
#         if x[i] > 0:
#             x[i] = "big"
#         else:
#             pass
#     return x
#
# print(convertbig([2,0,-1, 3, 5, -5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# (Note that zero is not considered to be a positive number).


# def countpositives(x):
#     count = 0
#     for i in range(len(x)):
#         if x[i] > 0:
#             count = count + 1
#     x[len(x)-1]=count
#     return x,count
# print(countpositives([1,6,-4,-2,-7,2]))



# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

# def sumoflist(x):
#     sum = 0
#     for i in range (len(x)):
#         sum = sum + x[i]
#         avg = sum/len(x)
#     return sum,avg
#
# print(sumoflist([6,3,3]))

# Length - Create a function that takes a list and returns the length of the list.


# def lenoflist(x):
#     count = 0
#     for i in x:
#         count = count + 1
#     return count
# print(lenoflist([6,3,3,5,6,6,7,7,8]))




# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.


# def minoflist(x):
#     min = 0
#     if len(x)<1:
#         return False
#     for i in range(len(x)):
#         if x[i] < min:
#             min = x[i]
#     return min
#
# print(minoflist([]))
# print(minoflist([37,2,1,-9,-18]))
#
#
#
# def maxoflist(x):
#     max = 0
#     if len(x)<1:
#         return False
#     for i in range(len(x)):
#         if x[i] > max:
#             max = x[i]
#     return max
#
# print(maxoflist([]))
# print(maxoflist([-3,-7,-2,1,-9,-18]))

#
# def reverselist(x):
#     y = len(x)
#     for i in range(int(len(x)/2)):
#         temp = x[y-1-i]
#         x[y-1-i] = x[i]
#         x[i] = temp
#     return x
#
# print(reverselist([1,3,4,-9,5,6]))
#
#
# def reversestring(x):
#     char = list(x)
#     y = len(char)
#     for i in range(int(y/2)):
#         temp = char[y-1-i]
#         char[y-1-i] = char[i]
#         char[i] = temp
#     return ''.join(reversed(char))
#
# print(reversestring("Pramod"))


x = "Pramodamododdd"
print(x.count("d"))
