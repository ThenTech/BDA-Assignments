amount_one_cent = int(input())
amount_two_cent = int(input())
amount_five_cent = int(input())
amount_ten_cent = int(input())
amount_twenty_cent = int(input())

total = (amount_one_cent + (amount_two_cent * 2) + (amount_five_cent * 5) + (amount_ten_cent * 10) + (amount_twenty_cent * 20))
euro = total // 100
first_cent = (total % 100) // 10
last_cent = (total % 100) % 10

print("You have ", euro, ".", first_cent, last_cent, " euro!", sep="")

