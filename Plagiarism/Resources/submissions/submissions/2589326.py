def lucky_numbers(number):
    empty_list = []
    for i in range(1,number+1):
        empty_list.append(i)


    for i in range(2,len(empty_list)):
        for element in range(1, len(empty_list[:])+1):
            if (element) % i == 0:
                if element in empty_list:
                    empty_list.remove(element)
    return empty_list

print(lucky_numbers(22))
