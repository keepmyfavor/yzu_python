
i = 1
while i < 10:
    j = 1
    while j < 10:
        print("%2d * %2d = %2d" % (i, j, i*j), end="")
        j += 1
    i += 1
    print()
