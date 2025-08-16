# 7. Find the second smallest and second largest element in an array

def second_large_small(arr):
    # sorting array
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    
    return arr,arr[-2],arr[1]

arr = [5,8,1,6,7,3]
arr,n1,n2 = second_large_small(arr)
print(f"your array is : {arr}")
print(f"Second highest : {n1} and second smallest : {n2}")