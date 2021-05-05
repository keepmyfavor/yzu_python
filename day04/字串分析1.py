# -*- coding:UTF-8 -*-

str = " she sell sea shell on teh sea shore "

print(str)
# 除去左右空白
str = str.strip()  # 去除左右空白
# str = str.lstrip()  # 去除左邊空白
# str = str.rstrip()  # 去除右邊空白
print(str)
print("字串長度:", len(str))
print("有幾個s:", str.count("s"))
print("有沒有on這個字的位置", str.find("on"))
print("有沒有off這個字的位置", str.find("off"))
print("有沒有sea這個字的位置", "有" if str.find("sea") >= 0 else '沒有')
print("有沒有land這個字的位置", "有" if str.find("land") >= 0 else '沒有')
print("有", str.count(" ") + 1, "個單字")
# 是否都是英文字(a-z, A-Z)
# 小技巧, 先利用replace 將中間的空白去除
print("是否都是英文字", str.replace(" ", "").isalpha())
print(str[2])
print(str[0:3])  # 取出0-3位置的字串,不含3(0, 1, 2)
path = r"C:\Users\LE-S41\PycharmProjects\yzu_python_20210414\day01\hello.py"
print("路徑位置:", path)
