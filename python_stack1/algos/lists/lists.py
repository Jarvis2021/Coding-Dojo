#  TO add String at the end of the List
#ninjas.append("Pramod-1")

# Pop() will remove the Value from the end of the String
#ninjas.pop()

# Pop(i) will remove the value for the index provided
#ninjas.pop(3)

# [] will slice based on the index values provided
ninjas = ["Pramod", "Conor", "Sashi", "Poori", "Bunny"]

# print(ninjas[3:])
numlist = [1,3,4,5,6,2,5,0,12,10,18]
#print(sorted(numlist))
# print(min(numlist))

ninjas.extend(numlist)

# print(ninjas)

def sum(x):
    return x+x

sumofnumbers = map(sum, numlist)

print(sumofnumbers)


# for i in enumerate(sorted(numlist)):
#     print i
