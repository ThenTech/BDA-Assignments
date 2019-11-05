word= input("woord: ")
def count_word(string):
    x=1
    for i in word:
          if i  == " ":
              x=x+1
    print(x)
count_word(word)