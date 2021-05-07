
for i in range(1, 10):
    for j in range(1, 10):
        # print("%2d * %2d = %2d" % (i, j, i * j))  # 直列九九乘法表
        print("|%2d * %2d = %2d|" % (j, i, i*j), end=" ")  # 橫列九九乘法表
    print()
