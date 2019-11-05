# write your code here
number = int(input("Give the length of the nucleabase."))

def nucleo_combinations(n):
    nucleostring = "ACGT"
    
    for i in nucleostring:
        if n == 1:
            print(i)
        else:
            print(i , nucleo_combinations(n-1), sep="", end="")
        
    return

nucleo_combinations(number)