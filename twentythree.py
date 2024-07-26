def bubblesort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)
a = [8,4,6,2,0,11,3]
print(bubblesort(a))
