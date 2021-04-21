# -*- coding:UTF-8 -*-
import keyword

# 保留字
print(keyword.kwlist)

print("我是中文")

'''
判斷成績是否及格
ctrl / 可一次多行註解

'''

score = 80
if score >= 60:
    print(score, "及格")
else:
    print(score, "不及格")

# 整數 8, 10, 16 進位表示
# PEP8 法則 空格要二格才不會有虛線
# 程式最後一行要留一行
a = 12  # 10進位
b = 0o12  # 8進位
c = 0x12  # 16進位

print(a, b, c)

# 浮點數
a = 3.14
b = 3.14e2  # 科學記號 3.14 * 10**2 (10的平方) 3.14e+2
c = 1000e-2  # 科學記號 1000 * 1/(10**2) (10的負2次方)
print(a, b, c)

# 賦值(=)
name, h, w, age, isPass = 'john', 170, 60, 18, True
print(name, h, "公分", w, "公斤",  age, "歲", isPass)

# 資料型態 (type)
print(name, type(name))
print(h, type(h))
print(w, type(w))
print(age, type(age))
print(isPass, type(isPass))

# 刪除變數
money = 1000000
print(money)
del money
# print(money) NameError: name 'money' is not defined
