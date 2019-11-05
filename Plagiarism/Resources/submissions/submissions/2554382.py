# write your code here


def seq(chars, length, prev):
    if length == 0:
        print( prev )
        return

    for char in chars:
        seq(chars, length-1, prev + char)


b = int(input())
seq("ACGT", b, "")