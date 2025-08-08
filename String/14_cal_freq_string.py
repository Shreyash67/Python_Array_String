# 14. Calculate frequency of characters in a string

def cal_freq_string(str1):
    dict1 = {}

    for ele in str1:
        if ele == ' ':
            continue
        else:
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=1
    
    return dict1

string = 'hello shreyash'
dict1 = cal_freq_string(string)

for k,v in dict1.items():
    print(f"{k} : {v}")