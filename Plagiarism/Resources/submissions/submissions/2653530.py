def convert(number):
   if len(number) ==1:
      return number
   for i in range(len(number)-1):
      x = function(number[len(number)-i-1])
      y = convert(number[:len(number)-1])
      w = 10 * int(y)+x
      return w
def function(i):
   d = ord(i) - ord("0")
   return d