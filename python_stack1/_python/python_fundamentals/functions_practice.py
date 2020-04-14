# x = []
# def countdown(n):
#     for i in range (n,-1,-1):
#         x.append(i)
#     return x
#
# print(countdown(5))


# def PR(x):
#     for i in range (0,len(x)):
#         if i < len(x):
#             print(x[i])
#         else: pass
#         return x[i+1]
# PR([1,2])

# def li(x):
#     if len(x) < 0:
#         print("not a valid list")
#     else:
#         return x[0] + len(x)
#
# print(li([1,2,3,4,5,6]))



# def newlist(x):
#     list2=[]
#     count = 0
#     if len(x)<2:
#         return "Not a Valid List"
#     for i in range(len(x)):
#         if x[i] > x[1]:
#             list2.append(x[i])
#             count = count + 1
#     return count,list2
#
# print(newlist([5,2,3,2,1,2,4]))
# print(newlist([6,2,3,5,4,10]))
# print(newlist([2]))


def repeatval(x,y):
    newlist = []
    for i in range(x):
        newlist.append(y)
    return newlist

print(repeatval(4,7))
print(repeatval(6,2))
print(repeatval(1,1))
