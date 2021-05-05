import random as r
# ans = 47
ans = r.randint(1, 99)
min = 0
max = 100
count = 5

while count > 0:
    print("還有%d次機會" % count)
    guess = int(input("請輸入%d ~ %d: " % (min, max)))
    # 檢查 guess 的資料是否在 min 與 max 之間
    if guess <= min or guess >= max:
        print("數字範圍錯誤")
        continue
    # 判定結果
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("答對了")
        break
    count -= 1
print("超過次數了,遊戲結束了,答案是%d" % ans)