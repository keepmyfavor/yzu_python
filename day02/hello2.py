# -*- coding:UTF-8 -*-

chinese = '100'  # str
english = '90'  # str
math = 80  # int
print(chinese, english, math)

print(type(chinese), type(english), type(math))
total = int(chinese) + int(english) + math  # 轉型才能運算
print("總分:", total)  # sum 是內置函數, 使用會有虛線
# TypeError: can only concatenate str (not "int") to str
print("總分:" + str(total))
