def replace(pattern, replacement, corpus):
    new_string = corpus.split()
    final_string = ""
    for word in new_string:
        if word != pattern:
            final_string += word
        else:
            final_string += replacement
        final_string += " "
    return final_string
