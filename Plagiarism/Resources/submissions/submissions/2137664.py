for nullvalue in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]:
    nullvalue = 0
word = input()
while lengte < len(word):
    for value in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]:
        if word[len(word) - 1 - lengte] == str(value):
            value += 1
    lengte += 1
for letter in  [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]:
    print(str(letter) + ": " + letter)