letter_list = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
counter = 0
s = input('String?')
for i in s:
    if i in letter_list:
        print(i, end='')
        counter += 1
    if i not in letter_list and counter != 0:
        print('', counter)
        counter = 0
if counter != 0:
    print('', counter)