import random as r

scores = [100, -10, 90, 80, 999]
# error_scores = scores.pop(1)
# print(error_scores, scores)
# error_scores = scores.pop(3)
# print(error_scores, scores)

new_scores = []
for x in scores:
    if x > 0 and x <= 100:
        new_scores.append(x)
print(new_scores)

# 利用 pop() 將不合法的分數挑出來
# 有BUG 會把index吃掉
# for x in scores:
#     if x < 0 or x > 100:
#         scores.pop(scores.index(x))
#         print("不合法的分數:", x)
# print(scores)

# 反轉
print(scores)
scores.reverse()
print(scores)

# 排序
scores.sort()
print(scores)

# 洗牌 import random
r.shuffle(scores)
print(scores)