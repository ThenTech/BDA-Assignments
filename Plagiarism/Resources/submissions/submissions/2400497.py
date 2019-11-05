def chop_pieces(string, i):
    indexing = i % len(string)
    return indexing


def create_sequence(string, index, length):
    word=""
    for i in range(index, index + length):
        word += string[chop_pieces(string, i)]

    return word