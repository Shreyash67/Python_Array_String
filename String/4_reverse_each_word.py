# 4. Reverse each word in string

def reverse_words(str1):
    word = str1.split()
    return " ".join([ele[::-1] for ele in word ])

str1 = "Hello shreyash"
print(reverse_words(str1))