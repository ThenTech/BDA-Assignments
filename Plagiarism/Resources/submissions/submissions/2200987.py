plaats=corpus.find(pattern)
def replace(pattern, replacement, corpus):
    while i != len(corpus-1):
        if plaats != corpus.find(pattern, i):
            print(corpus[:plaats], replacement, corpus[(plaats+len(pattern)):]
            plaats=corpus.find(pattern, i)
        i+=1
    