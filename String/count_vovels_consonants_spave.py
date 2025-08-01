# 5. Count number of vowels, consonants, spaces in String

def count_vow_cons_spc(str1):
    vovels = ['a','e','i','o','u','A','E','I','O','U']
    v_count = 0
    cons_count = 0
    spc_count = 0

    for char in str1:
        if char==' ':
            spc_count+=1
        elif char in vovels:
            v_count+=1
        else:
            cons_count+=1
    
    return v_count,cons_count,spc_count

str1 = "hello shreyash"
a,b,c = count_vow_cons_spc(str1)
print(f"Vovels : {a}, Consonant : {b}, Space : {c}")