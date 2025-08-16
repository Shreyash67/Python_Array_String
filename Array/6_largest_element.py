# 6. Find the largest number in an array

def largest_element(arr):
    max = arr[0]

    for ele in arr:
        if ele>max:
            max = ele
    
    return max

arr = [7,5,2,3,6,0,11]
ans = largest_element(arr)
print(ans)