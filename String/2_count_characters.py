# 2. Count the occurrence of a character in string

def count_character(sentence):
    dict1 = {}
    sentence = sentence.lower()
    sentence = sentence.replace(" ","")
    
    for ele in sentence:
        if ele in dict1:
            dict1[ele]+=1
        else:
            dict1[ele]=1
    
    return dict1

sentence = "Hello dear friend"
result = count_character(sentence)

for key,value in result.items():
    print(f"{key} : {value}")