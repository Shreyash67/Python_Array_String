# 1. Check if a given string is palindrome or not

def palindrome(str1):
    if str1 == str1[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

str1 = input("Enter the string : ")
result = palindrome(str1)
print(result)