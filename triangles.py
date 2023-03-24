x = 1
tris = 6

while x <= 9:
    x += 1
    tris += 6 * (2 * x - 1)
    print(x, ' ', tris)
