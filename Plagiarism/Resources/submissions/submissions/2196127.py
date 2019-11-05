sentence = "Python! programming     ....  ROCKS"
punctuation_and_number = '''123456789!\"#$%&'()*+,-”./:’;<“=>?@[\\]^_`{|}~ '''
enter = ""
string_without_punct = ""
end = 0
start = 0
counter = 0
for letter in sentence:
    if letter not in punctuation_and_number:
        string_without_punct = string_without_punct + letter
        end = end + 1
        counter = counter + 1
    if letter in punctuation_and_number and letter != " ":
        if start != end:
            print(string_without_punct[start:], counter)
            start = end
            counter = 0
print(string_without_punct[start:], counter)
