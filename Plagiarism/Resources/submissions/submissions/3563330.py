# write your code here
a=input("give a sentence")
b = ""
count = 0
for i in range(len(a)):
    if a[i] <= "z" and a[i] >= "A":
        b+=a[i]
        count+=1
    if i+1< (len(a)-1):
        if a[i+1] > "z" and a[i + 1] < "A" and a[i + 2] <= "z" and a[i + 2] >= "A" :
            print(b + " " + str(count))
            count=0
            b=""
    if i==(len(a)-1):
        print(b + " " + str(count))