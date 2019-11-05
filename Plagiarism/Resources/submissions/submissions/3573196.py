# write your code here

def make_sub(string):
    if len(string) <= 1:
        return string
    print(make_sub(string[2:]))
    print(string[:2] + make_sub(string[2:]))

x = input("")

make_sub(x)
