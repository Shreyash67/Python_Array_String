# 6. Find the ASCII value of a character

def ascii(char):
    small_alpha = "abcdefghijklmnopqrstuvwxyz"
    Capital_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0

    if char in small_alpha:
        for i in range(len(small_alpha)):
            if small_alpha[i]==char:
                count+=1
                return 96+count
            else:
                count +=1
    else:
        for i in range(len(Capital_alpha)):
            if Capital_alpha[i]==char:
                count+=1
                return 64+count
            else:
                count +=1

char = "Z"
print(ascii(char))