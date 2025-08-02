# 8. Remove spaces from a string

def remove_space(string):
    new_string = ""
    for char in string:
        if char == " ":
            continue
        else:
            new_string+=char
    
    return new_string

print(remove_space("India is my country"))