def lucky_numbers(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    print(list)
    maxcount = 2
    while(maxcount < len(list)):
        count = 0
        newlist = []
        for j in range(len(list)):
            count+=1
            if(count != maxcount):
                newlist.append(list[j])
            else:
                count = 0
        maxcount+=1
        list = newlist
    print(list)