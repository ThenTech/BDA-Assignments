w1 = input("")
w2 = input("")

def counter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

i = 0

while i < len(w1):
    if "a" <= w1[i] <= "z" and counter(w1, w1[i]) != counter(w2, w1[i]):
        print(w1, 'and', w2, "are not anagrams")
        break
    elif i == len(w1) - 1:
        print(w1, 'and', w2, "are anagrams")