def is_palindrome_sentence123(sentence):
   lower = sentence.lower()
   sentence = ""
   for i in lower:
      if i != " ":
         sentence += i
   for i in range(len(sentence)//2):
      if sentence[i] != sentence[len(sentence)-1-i]:
         return False 
   return True
       
def is_palindrome_sentence(sentence)
if (is_palindrome_sentence123(sentence)):
    return True
else:
    return False
