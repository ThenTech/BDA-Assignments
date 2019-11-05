def is_palindrome_sentence(sentence):
    sentence = make_string(sentence)
    for i in range(len(sentence)//2):
        if sentence[i] == sentence[((len(sentence)-1) - i)]:
            continue
        else:
            return False
    return True

def make_string(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    drukletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in sentence:
        if i in letters or i in drukletters:
            result += i
    result2 = ""
    for i in range(len(result)):
        if result[i] in drukletters:
            for x in drukletters:
                if x == result[i]:
                    global index
                    index = i
                    break
            result2 += letters[index]
        else:
            result2 += result[i]
    return result2