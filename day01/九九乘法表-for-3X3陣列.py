
for k in range(0, 3):
    for i in range(1, 10):
        for j in range(3 * k + 1, 3 * k + 4):
            print("%2d * %2d = %2d " % (j, i, i*j), end = (" "))
        print()
    print()