def shift(lstinput, places):
	lstoutput = []
	places = places*(-1)
	places %= len(lstinput)
	lstoutput += lstinput[places:]
	lstoutput += lstinput[:places]
	return lstoutput