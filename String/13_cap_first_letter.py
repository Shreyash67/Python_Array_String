# 13. Capitalize first and last character of each word

sent = 'hello bro my name is shreyash'

sent_list = sent.split()

new_sent = ''

for i in range(len(sent_list)):
    word = sent_list[i]
    
    if len(word) == 1:
        new_sent += chr(ord(word[0])-32)
    else:
        first_capital = chr(ord(word[0])-32)
        last_capital = chr(ord(word[-1])-32)
        middle_part = word[1:-1]

        new_sent = new_sent + first_capital + middle_part + last_capital

    new_sent += " "

print(new_sent)