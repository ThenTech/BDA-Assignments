def lucky_numbers(length):
    numbers = [number for number in range(1, length + 1)]
    print(numbers)
    counter = 2
    for element in range(0, length):

        if len(numbers) < element:
            break

        newCounter = 0
        length = len(numbers)
        for item in range(counter, length + 1, counter):
            del numbers[item - 1 - newCounter]
            newCounter += 1

        counter += 1
    return numbers