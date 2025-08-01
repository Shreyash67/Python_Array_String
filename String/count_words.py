# 3. Count word in string

def count_words(sentence):
    words = sentence.split()
    return len(words)
    
sentence = "My name is Shreyash"
print(count_words(sentence))