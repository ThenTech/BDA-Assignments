def count_words(Hello):
    content = Hello.read()
    Hello.close()

    words = content.split
    print(len(words))
    