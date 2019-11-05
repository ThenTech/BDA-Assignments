def merge_lists(number, merged_list):  # insert de 1-delige lijsten in de merged_list
    for i in range(len(merged_list) + 1):
        if number[0] > merged_list[i]:
            continue
        else:
            return merged_list.insert(i, number[0])


def merge_sort1(list, merged_list):  # maakt 1-delige lijsten van de originele lijst
    if len(list) > 1:
        list_a = merge_sort1(list[:int(len(list) / 2)], merged_list)
        list_b = merge_sort1(list[int(len(list) / 2):], merged_list)
    else:
        return merge_lists(list, merged_list)
    if len(merged_list[:len(merged_list) - 1]) == len(list):
        return merged_list[:len(merged_list) - 1]


def merge_sort(list):
    return merge_sort1(list, [999])