def linear_search(list1,target):
    s = 0
    e = len(list1)-1

    while s<=e:
        if list1[s]==target:
            return 1
        else:
            s = s + 1
    return -1

list1 = [4,8,9,1,0,3]
target = 3

ans = linear_search(list1,target)

if ans==True:
    print("found")
else:
    print("Not Found")