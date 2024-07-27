def bubblesort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)
a = [8,4,6,2,0,11,3]
print(bubblesort(a), 'bubble sort')

def insort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        else:
            arr[j+1]=key
    print(f'sorted list: {arr} insertion sort')
insort(a)