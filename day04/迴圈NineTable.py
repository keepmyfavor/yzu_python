# x*y=z
# 1*1=1 1*2=2 ... 1*9=3
# 9*1=9 9*2=18 ... 9*9=81

n = int(input("請輸入乘法表size: ")) + 1

for x in range(1, n):
    for y in range(1, n):
        z = x * y
        # print("%d*%d=%d" % (x, y, z))
        print("%2d*%-2d=%2d" % (x, y, z), end=" ")  # 02d 最多二個0, 不足補0, 不加0, 就是空格, -2, 是左往右放
    print()

