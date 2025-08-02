# 10. Reverse a String

def reverse_string(str1):
    str2 = ""
    for i in range(len(str1)):
        str2+=str1[len(str1)-1-i]
    return str2

str1 = "hello"
print(reverse_string(str1))