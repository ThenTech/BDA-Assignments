def convert(number):
	if len(number) > 0:
		return (int(number[0]) *10 ** len(number[1:]) + convert(number[1:]))
	else:
		return 0