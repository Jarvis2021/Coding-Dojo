# Find and Replace

words = "It's thanksgiving day. It's my birthday, too"

print(words.find("day"))
print(words.replace("day", "month",1))

# Min and Max
def minandmax(x):
    if len(x)<1:
        return "Not a Valid List"
    else:
        return min(x), max(x)

print(minandmax([0]))

# First and Last

x = ["hello",2,54,-2,7,12,98,"world"]

def sortandprint(x):
    y = []
    y.append(x[0])
    y.append(x[len(x)-1])
    return y

print (sortandprint(x))

#New List

x = [19,2,54,-2,7,12,98,32,10,-3,6]

def newlist(x):
    x.sort()
    firstlist = x[:len(x)/2]
    secondlist = x[len(x)/2:]
    secondlist.insert(0, firstlist)

    return firstlist, secondlist

print(newlist(x))
