def lucky_numbers(n):
    luckyNumbers = [i+1 for i in range(n)]
    
    removeElement = 2
    position = 0
    
    while removeElement < len(luckyNumbers):
        for i in luckyNumbers[:]:
            if (position+1) % removeElement == 0 and position != 0:
                luckyNumbers.remove(i)
            position += 1
        removeElement += 1
        position = 0
    return luckyNumbers