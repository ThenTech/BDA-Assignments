def encode(mijnen):
    stringding=""
    gecodeerd=""
    if int(len(mijnen))==1:
        return "0"
    else:
        for n in range(len(mijnen)):
            if n == 0:
                if mijnen[n+1] == "X":
                    gecodeerd = gecodeerd + "1"
                else:
                    gecodeerd = gecodeerd + "0"

            elif n==len(mijnen)-1:
                if mijnen[n-1] == "X":
                    gecodeerd = gecodeerd + "1"
                else:
                    gecodeerd = gecodeerd + "0"
            else:
                if mijnen[n-1] == "X" and mijnen[n+1] == "X":
                    gecodeerd = gecodeerd + "2"
                elif mijnen[n-1] == "X" or mijnen[n+1] == "X":
                    gecodeerd = gecodeerd + "1"
                else:
                    gecodeerd = gecodeerd + "0"
    return gecodeerd


def decode(s, n):
    pass