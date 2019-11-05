input1 = input()
input2 = input()
i = 0
j = 0

while (True):
    if input1[i] != input2[j]:
        j += 1
        continue
    elif j == len(input1):
        print(input1,'and', input2, 'are not anagrams')
        break
    elif i == len(input1)-1:
        print(input1, 'and', input2, 'are anagrams')
        break
    else:
        i += 1
        j = 0
        continue