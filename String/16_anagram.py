# 16. Check if two strings are anagram of each other

def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
       
    for ele in str1:
        count1 = 0
        count2 = 0

        for ch in str1:
            if ch==ele:
                count1+=1
        
        for ch in str2:
            if ch==ele:
                count2+=1
        
        if count1!=count2:
            return False
    
    return True
        
str1 = 'soon'
str2 = 'nose'

ans = anagram(str1,str2)

if ans==True:
    print("Anagram")
else:
    print("Not Anagram")