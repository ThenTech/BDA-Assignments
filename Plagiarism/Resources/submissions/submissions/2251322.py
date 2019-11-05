def encode(input_string):
    encoded_str = ""

    for index in range(len(input_string)):
        line_count = 0
        if index == 0 and len(input_string) > 1:
            if input_string[index + 1] == "X":
                line_count += 1
        elif index == len(input_string) - 1 and len(input_string) > 1:
            if input_string[index - 1] == "X":
                line_count += 1
        elif len(input_string) > 2:
            if input_string[index - 1] == "X":
                line_count += 1
            if input_string[index + 1] == "X":
                line_count += 1

        encoded_str += str(line_count)

    return encoded_str

def decode(input_string):
    str_len = len(input_string)

    for element in brute_force(" X", str_len):
        if encode(element) == input_string:
            print(element)


def brute_force(chars, length):
    forced_list = [(chars[0]) * length]
    new_list = []

    # Gaat over de lengte van de te bruteforcen string
    # Voeg de nieuwe lijst tijd aan de oude en maak de nieuwe leeg zodat je het process kan herhalen
    for current in range(length):

        # Ga voor elk te gebruiken character alle stappen af
        for index in range(1, len(chars)):

            # Per element in de lijst, maak een nieuw element aan en pas het i(de) of current character aan en voeg dit toe aan de lijst
            for element in forced_list:
                new_force = ""
                # Pas het character op huidige positie aan naar het huidige character van het element in de lijst
                for el_index in range(len(element)):
                    if el_index == current:
                        new_force += chars[index]
                    else:
                        new_force += element[el_index]
                new_list.append(new_force)
        forced_list += new_list
        new_list = []

    return forced_list
