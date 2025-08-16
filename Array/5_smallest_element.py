# 5. Find the smallest number in an array

def smallest_element(arr):
    min = arr[0]

    for ele in arr:
        if ele<min:
            min = ele
    
    return min

arr = [7,5,2,3,6,0]
ans = smallest_element(arr)
print(ans)
