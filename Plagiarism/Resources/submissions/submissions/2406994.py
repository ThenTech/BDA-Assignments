def convert(number):
   if len(number) > 0:
      print(number[0],end="")
      convert(number[1:])