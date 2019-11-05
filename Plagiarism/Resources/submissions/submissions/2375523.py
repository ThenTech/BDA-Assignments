# write your code here
word_1=input("give a word")
word_2=input("give a word")
total=0
for i in range(len(word_1)):
    for j in range(len(word_2)):
        if word_1[i]==word_2[j]:
            total+=1
            if total==len(word_1):
                print(word_1 + " and " + word_2 + " are anagrams")
            else:
                print(word_1 + " and " + word_2 + " are not anagrams")
                