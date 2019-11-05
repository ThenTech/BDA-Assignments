textA = input()
textB = input()
textAS = sorted(textA)
textBS = sorted(textB)

isAna = True

if len(textAS) != len(textBS):
    isAna = False
else:
    for i in range(0, len(textAS)):
        if textAS[i] != textBS[i]:
            isAna = False
            break

if isAna:
    print(textA + " and " + textB + " are anagrams")
else:
    print(textA + " and " + textB + " are not anagrams")
