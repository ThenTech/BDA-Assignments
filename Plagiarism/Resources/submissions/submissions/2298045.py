def lucky_numbers(n):
   m = range(1,n+1)
   l = []
   for x in m:
      l.append(x)
   for i in range(2,n):
      if len(l) <= i:
        return l
      else: 
        for a in l:
           if a % i == 0:
              l.remove(a)  