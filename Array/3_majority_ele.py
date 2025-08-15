# 3. Find the majority element in an array

def majority(arr):
    dict1 = {}

    n = len(arr)//2

    for ele in arr:
        if ele in dict1:
            dict1[ele]+=1
        else:
            dict1[ele]=1
    
    for k,v in dict1.items():
        if v>n:
            return k
    else:
        return None

arr = [3, 3, 4, 2, 3, 3, 5]
ans = majority(arr)
print(ans)
