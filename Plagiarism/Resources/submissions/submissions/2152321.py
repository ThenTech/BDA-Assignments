cent1 = int(input()) * 1
cent2 = int(input()) * 2
cent5 = int(input()) * 5
cent10 = int(input()) * 10
cent20 = int(input()) * 20
total = cent1 + cent2 + cent5 + cent10 + cent20

euro = total // 100
tenc = (total % 100) // 10
onec = total % 10

print("You have ", euro, ".", tenc, onec, " euro!", sep='')