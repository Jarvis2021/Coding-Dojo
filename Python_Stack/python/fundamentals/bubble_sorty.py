x = [15,14,16,13,8,7,5,3,0,1,2,4,6,13,12,11,9,10]

def bubblesort(x):
    count = 0
    for j in range (len(x)-1):
        for i in range(len(x)-1-j):
            if x[i] > x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
            else:
                pass
            count = count + 1
    print count
    return x



print(bubblesort(x))
