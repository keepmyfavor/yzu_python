# -*- coding:UTF-8 -*-

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n == 0 or n == 1:
    #   return n
    return fib(n-1) + fib(n-2)

n = 30
value = fib(n)
print(n, value)

x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

head = 83  # 總頭
foot = 240  # 總腳
y = (foot - 2 * head) / 2  # 計算多出的腳
x = head-y  # 計算出雞的數量
print("雞有 %d 只 兔有 %d 只" % (x, y))
