# write your code here
def write_words(ss):
    word = ""
    ss += " "
    for i in ss:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            word += i
        else:
            if word != "":
                print(word, len(word))
                word = ""


write_words(input())