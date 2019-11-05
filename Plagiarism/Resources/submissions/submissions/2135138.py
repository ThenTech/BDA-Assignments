# write your code here

string = input("input string:")
i = 0

while i <= len(string) - 1:
    print(string[len(string) - 1 - i], end="")
    i += 1
    