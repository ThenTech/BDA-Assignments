def create_sequence(string, index, length):
    # Take absolute value of index
    number = ""
    for i in str(index):
        if i != "-":
            number += i
    number = int(number)

    # Calculate the index on which the sequence should start
    start_index = len(string) % number

    # Convert the string to start with the required letter
    head = string[start_index:]
    tail = string[:start_index]
    new_string = head + tail

    # Calculate how many times the full string is needed and make the sequence
    if length <= len(string):
        amount = 1
    else:
        amount = (length // len(string)) + 1

    sequence = new_string * amount

    # Cutting the sequence to the required length
    sequence = sequence[0:length]
    return sequence