def create_sequence(string, index, lengte):
    geheel_woord = ""
    for el in range(int(index), int(index+lengte)):
        index_nieuw = el%len(string)
        geheel_woord = geheel_woord + string[index_nieuw]
    return geheel_woord
