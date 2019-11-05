def encode(minefield):
    encoded = ""

    for i in range(len(minefield)):
        if i == 0:
            if len(minefield) <= 1:
                break
            elif minefield[i + 1] == "X":
                encoded += str(1)
        elif i == len(minefield) - 1:
            if minefield[i - 1] == "X":
                encoded += str(1)
        else:
            counter = 0
            if minefield[i-1] == "X":
                counter += 1
            if minefield[i+1] == "X":
                counter += 1
            encoded += str(counter)
    return encoded


def decode(minefield):
    decoded = ""

    for i in range(2 ** len(minefield)):
        for j in range(len(minefield)):
            if (i // 2**j) % 2 == 1:
                decoded += "X"
            else:
                decoded += " "
        if encode(decoded) == minefield:
            print(decoded)
        decoded = ""
