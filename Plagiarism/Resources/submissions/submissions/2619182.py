n = int(input())
alfabet = "ACGT"
string = ""
def function(alfabet,n,string):
    if len(string) == n:
       print(string)
    else:
        for i in alfabet:
           function(alfabet,n,string+i)
function(alfabet, n ,string)
