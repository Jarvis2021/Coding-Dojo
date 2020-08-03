# Assignment: Compare Lists

l1 = [1,2,5]
l2 = [1,2,5,6,2]


def comparelists(x,y):

    if len(x) <> len(y):
        return "List Length Doesn't match"

    if l1==l2:
        print ("Lists are identical")
    else:
        print("Lists are not identical")

print(comparelists(l1,l2))
