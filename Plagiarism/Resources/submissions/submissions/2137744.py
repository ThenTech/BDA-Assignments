# write your code here

string_a = input("Give me the first string: ")
string_b = input("Give me the second string: ")

err = False

for current_letter in "abcdefghijklmnopqrstuvwxyz":

    amount_a = 0
    amount_b = 0

    for index_a in range(len(string_a)):
        if current_letter == string_a[index_a]:
            amount_a += 1

    for index_b in range(len(string_b)):
        if current_letter == string_b[index_b]:
            amount_b += 1

    if amount_a != amount_b:
        err = True

if err:
    print(string_a, "and", string_b, "are not anagrams")
else:
    print(string_a, "and", string_b, "are anagrams")