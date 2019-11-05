def count_letter(x):
    for i in range(ord('z')-ord('a')+1):
        print(chr(ord('a')+i) + ":", x.count(chr(ord('a')+i)))

count_letter(input())