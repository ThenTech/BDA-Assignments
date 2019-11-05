def is_ordered(lijst):
    nieuwlijst = lijst[:]
    nieuwlijst.sort()
    if nieuwlijst == lijst:
        return True
    else:
        return False