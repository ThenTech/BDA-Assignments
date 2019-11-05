def lucky_numbers(n):
    for i in n[1:]:
      for x in n:
        if x % i ==0:
            if len(n) > i:
               n.remove(x)
            else:
               return n