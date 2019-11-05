def is_ordered(lstToCheck):
	correctorder = True
	if len(lstToCheck) < 0:
		lastnumber = lstToCheck[0]
		for number in lstToCheck:
			if number < lastnumber:
				correctorder = False
			lastnumber = number
	return correctorder