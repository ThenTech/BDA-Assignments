n = int(input("Amount of nucleobases in one combination:"))

def find_combinations(n):
    bases = ["A", "C", "G", "T"]
    combinations = []

    for base in bases:
        if n > 1:
            secondbases = find_combinations(n-1)
            for newbase in secondbases:
                combinations.append(base + newbase)

        else:
            combinations.append(base)

    return combinations

result = find_combinations(n)

for combination in result:
    print(combination)