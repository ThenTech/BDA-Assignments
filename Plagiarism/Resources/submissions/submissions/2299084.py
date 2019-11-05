def shift(lstinput, places):
	if len(lstinput) == 0:
		return 
	places = places*(-1)
	places %= len(lstinput)
	lstoutput = lstinput[places:]
	lstoutput += lstinput[:places]
	return lstoutput