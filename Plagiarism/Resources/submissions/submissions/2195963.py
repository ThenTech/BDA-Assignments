def is_palindrome_sentence(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    in_alphabet = False
    sum = ""
    palindrome = True
    sentence = sentence.upper()
    for i in sentence:
        for j in alphabet:
            if i == j:
                in_alphabet = True
        if in_alphabet:
            sum += j
        in_alphabet = False
    for i in (0, len(sum) - 1):
        if sum == "":
            palindrome = True
        if sum != "" and sum[i] == sum[len(sum) -1 - i]:
            palindrome = palindrome and True
        else:
            palindrome = False
    return palindrome