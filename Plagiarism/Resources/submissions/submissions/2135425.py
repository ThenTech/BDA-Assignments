string = input('String ')
lijst_string = list(string)
for el in range(len(string)):
    print(lijst_string[len(string)-1-el], end="")