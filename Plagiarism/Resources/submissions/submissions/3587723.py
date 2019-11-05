def lucky_numbers(n):
    list = []
    for i in range(n):
        list.append(i)
    
    count = 2
    add = 2
    while count < len(list):
        for i in range(len(list)):
            if i % count == 0:
                list.remove(i)
            count += add
        add +=1
        count = add