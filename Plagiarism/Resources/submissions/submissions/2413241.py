# write your code here
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
    
n = input()
elements = brute_force("ACGT", n)
    
for el in elements:
    print(el)