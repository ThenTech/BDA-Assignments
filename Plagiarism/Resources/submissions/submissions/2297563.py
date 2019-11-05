def is_ordered(lstToCheck):
	correctorder = True
	lastnumber = lstToCheck[0]
	for number in lstToCheck:
		if number < lastnumber:
			correctorder = False
		lastnumber = number
	return correctorder