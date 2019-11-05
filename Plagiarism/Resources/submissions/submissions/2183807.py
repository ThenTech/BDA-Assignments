def substring(x, y, z):
    print(x[y:y+z])

def find_pos(x, y):
    print(y.find(x))

def in_string(x, y):
    if y.count(x) > 0:
        print("True")
    else:
        print("False")