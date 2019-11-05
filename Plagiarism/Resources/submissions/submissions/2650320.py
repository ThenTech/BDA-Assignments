def DNA_keten(length, prefix):
    if len(prefix) == length:
        print(prefix)
    else:
        for char in "ACGT":
            DNA_keten(length, prefix + char)

x = int(input(""))
DNA_keten(x, "")