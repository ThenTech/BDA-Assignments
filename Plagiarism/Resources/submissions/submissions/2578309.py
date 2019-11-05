def replace(pattern, replacement, corpus):
    for i in range(len(corpus)-len(pattern)):
            if pattern == corpus[i:i+len(pattern)]:
                location = i
                break
    print(corpus[0:location], replacement,corpus[location+len(pattern):], sep ="")