def convert(number):
  if number:
    return (ord(number[-1]) - ord('0')) + 10 * convert(number[:-1])
  else:
    return 0
