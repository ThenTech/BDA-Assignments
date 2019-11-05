def is_unique(l):
    for i in range(len(l)):
        return not(l[i] in l[0:i] or l[i] in l[i+1:len(l)])