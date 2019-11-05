def subset(l):
	subset_helper(l, [])

def subset_helper(l, result):
    if len(l) == 0:	
        print(result)
    else:
	    eerste = l[0]
	    rest = l[1:]
		# niet toevoegen
		subset_helper(rest, result)
		#  toevoegen
		subset_helper(rest, result + [eerste])

subset(input())