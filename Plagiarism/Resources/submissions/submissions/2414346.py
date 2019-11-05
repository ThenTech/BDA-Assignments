def print_helper (length,alpabeth, prefix):
   if (len(prefix) ==length):
      print(prefix)
   else:
      for char in alpabeth:
         print_helper(length, alpabeth,prefix +char)
def print_dna(length):
   bases ="ACGT"
   print_helper(length, bases, "")
print_dna(int(input()))