a = input()
b = input()
m = "are anagrams"

def get_letters_list(a):
    a_ls = a.split()
    a_list = []
    for i in a_ls:
        for j in i:
            if 'a' <= j <= 'z':
                a_list.append(j)
    a_list.sort()
    return a_list


def sort_list(ls):
    ls.sort()
    return ls


if not (sort_list(get_letters_list(a)) == sort_list(get_letters_list(b))):
    m = "are not anagrams"

print(a, "and", b, m)