# write your code here
a=input("give a sentence")
b = ""
count = 0
for i in range(len(a)):
    if a[i] in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
        b+=a[i]
        count+=1
    if i+1< (len(a)-1):
        if a[i+1] not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN" and a[i+2] in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
            print(b + " " + str(count))
            count=0
            b=""
    if i==(len(a)-1):
        print(b + " " + str(count))