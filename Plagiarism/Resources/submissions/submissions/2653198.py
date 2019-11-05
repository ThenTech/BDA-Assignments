def is_magic_square(m):
   if len(m)%2 == 0:
      return False
   for i in m:
      if len(i) != len(m):
         return False
   if function2(m) == False or function3(m) == False or function4(m)==False:
      return False
   else:
      return True
def function2(m):
   p = 0
   n = 0 
   for i in m:
      n = p
      p = 0
      for j in i:
         p += j
      if n != 0:
         if n != p:
            return False
def function3(m):
   p = 0
   n = 0
   for i in range(len(m)):
      n = p
      p = 0
      for j in range(len(m)):
         p += m[j][i]
      if n != 0:
         if n != p:
            return False
def function4(m):
   p = 0
   n = 0
   for i in range(len(m)):
      p += m[i][i]
      n += m[len(m)-1-i][len(m)-1-i]
   if n != p:
      return False