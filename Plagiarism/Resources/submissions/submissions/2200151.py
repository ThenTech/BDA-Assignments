punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
def is_palindrome_sentence(sentence):
    s_without = ""
   
    for letter in sentence:
        if letter not in punctuation:
            s_without += letter
    
    
   
    qp = is_palindrome_sentence("").upper()
    for reverse in range(len(qp)):
        pq= qp[len(qp)-1-reverse]

    def gelijk(pp, pq):
        pp = is_palindrome_sentence("").upper()
        qp = is_palindrome_sentence("").upper()
        for reverse in range(len(qp)):
            pq = qp[len(qp)-1-reverse]
        if pp == pq:
            return True
    