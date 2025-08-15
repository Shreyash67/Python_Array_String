# 1.Search the element in an array (Binary search)

def binary_search(list1,target):
    list1 = sorted(list1)
    s = 0
    e = len(list1)-1

    while s<=e:
        m = (s+e)//2

        if list1[m]==target:
            return 1
        elif list1[m]<target:
            s=m+1
        else:
            e=m-1
    return -1

list1 = [4,8,9,1,0,3]
target = 0

ans = binary_search(list1,target)

if ans:
    print("found")
else:
    print("Not Found")