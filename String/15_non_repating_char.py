# 15. Find Non-repeating characters of a String

def non_rep_char(string):
    dict1 = {}
    non_rep_char = []
    
    for ele in string:
        if ele == ' ':
            continue
        else:
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=1
    
    for k,v in dict1.items():
        if v==1:
            non_rep_char.append(k)
    
    return non_rep_char

non_rep_char = non_rep_char('hello shreyash')

print(non_rep_char)