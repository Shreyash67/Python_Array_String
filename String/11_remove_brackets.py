# 11. Remove brackets from an algebraic expression

def remove_brackets(expression):
    brackets = ['(',')','[',']','{','}']
    new_expression = ''

    for ele in expression:
        if ele not in brackets:
            new_expression+=ele
    
    return new_expression

exp = '(a+b)+(c-d)'
print(remove_brackets(exp))