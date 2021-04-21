# -*- coding:UTF-8 -*-

# 隨機亂數
import random

n = random.randrange(0, 5)  # 0 <= n < 5 (0, 1, 2, 3, 4)
print(n)
n = random.randint(0, 5)  # 0 <= n <= 5 (0, 1, 2, 3, 4, 5) 比較直覺
print(n)
n = random.randint(10, 20)  # 取小數
print(n/10)

# 四星彩電腦選號
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4)

# 跳脫字元
print("小明\n明天\t要跟\"小英\"結婚了")
print("小明\\n明天\\t要跟\\\"小英\\\"結婚了")
