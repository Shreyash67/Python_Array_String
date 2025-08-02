# 9. Remove characters from a string except alphabets

def remove_char_exp_alpha(str1):

    new_string = ""

    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in str1:
        if char in alphabets:
            new_string+=char

    return new_string

string = "Hello@ 11"
print(remove_char_exp_alpha(string))