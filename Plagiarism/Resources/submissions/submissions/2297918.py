def fibonacci_values(i):
	fibonaccisequence = [0, 1]
	for n in range(2,i):
		fibonaccisequence += [(fibonaccisequence[n-2] + fibonaccisequence[n-1])]
	return fibonaccisequence