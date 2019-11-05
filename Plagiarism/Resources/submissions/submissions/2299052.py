def shift(lstinput, places):
	places = places*(-1)
	places %= len(lstinput)
	lstoutput = lstinput[places:]
	lstoutput += lstinput[:places]
	return lstoutput