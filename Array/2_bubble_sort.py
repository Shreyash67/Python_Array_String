# 2. Sort element in an array (Bubble sort)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr
    
arr = [5, 3, 8, 4]
ans = bubble_sort(arr)
print(ans)