import random as r
lotto = set()  # 不重複元素的串列
lotto.add(10)
lotto.add(10)
lotto.add(20)
print(len(lotto), lotto)

# 今彩539電腦選號, 1~39取出任意5個不重複的號碼
lotto = set()
while len(lotto) < 5:
    n = r.randint(1, 39)
    lotto.add(n)
print(lotto)

