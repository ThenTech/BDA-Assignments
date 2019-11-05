subset_list = []


def print_subsets(numbers, current_number, current_subset_list):
    global subset_list
    print(current_number)

    if len(current_number) == 0:
        return
    else:
        subset_list.append(current_number)

    if len(subset_list) >= 2:
        if len(current_number) > 1:
            return
        else:
            for subset in current_subset_list:
                print_subsets(numbers, current_number + " " + subset, current_subset_list)

    if subset_list[-1] == numbers:
        return


def get_number(numbers):
    global subset_list
    print_subsets(numbers, '', subset_list)
    for number in reverse(numbers):
        if number is not ' ':
            current_subset_list = subset_list[:]
            print_subsets(numbers, number, current_subset_list)


def reverse(string):
    reversed_list = []
    for char in string:
        reversed_list[0:0] = char
    return reversed_list


numbers = input('Numbers: ')
get_number(numbers)