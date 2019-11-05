def is_unique(lista):
  
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            if lista[i] == lista[j] and i != j:
                return False

    return True