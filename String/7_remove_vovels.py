# 7. Remove all vowels from the string

def string(str1):
    vovels = ['a','e','i','o','u','A','E','I','O','U']

    my_string = ''

    for ele in str1:
        if ele not in vovels:
            my_string = my_string + ele
    
    return my_string

print(string("shreyash"))