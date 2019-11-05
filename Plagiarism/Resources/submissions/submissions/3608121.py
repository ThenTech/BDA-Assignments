# write your code here
number = int(input("Give the length of the nucleabase."))

def nucleo_combinations(n):
    nucleostring = "ACGT"
    
    for i in nucleostring:
        for j in nucleostring:
            if n == 1: 
                print(i)
            else:
                print(i, j, sep="")
    if n > 1:
        nucleo_combinations(n-1)
    return

nucleo_combinations(number)