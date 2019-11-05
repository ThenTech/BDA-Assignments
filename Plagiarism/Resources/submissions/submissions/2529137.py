def print_helper(max, length, list):
    if len(list) == length:
        a = ""
        for i in list:
            a += str(i) + " "
        print(a[:len(a)-1])
        return
    else:
        for i in range(max):
            highest_number = max
            max = max - 1
            new_list = list + [highest_number]
            print_helper(max, length, new_list)




def print_dna(max, length):
    print_helper(max,length, [])


print_dna(int(input("max")), int(input("lenght")))