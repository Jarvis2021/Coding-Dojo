# Bubble Sort

def bubblesort(arr):
    count=0
    for j in range (0,len(arr)-1):
        for i in range(0,len(arr)-1-j):
            count +=1
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                # print("Swapped array:", arr)
            else: pass
    return arr,count

print(bubblesort([9,8,7,32,6,5]))


# Selection Sort
x = [4,6,2,9,1,7,8,0,3,5,-4,-2]

def selectsort(x):
    for i in range (len(x)):
        min = i
        for j in range (i+1,len(x)):
            if x[j] < x[i]:
                min = j
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x

print(selectsort(x))
