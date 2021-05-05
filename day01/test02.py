# 題目：輸入某年某月某日，判斷這一天是這一年的第幾天？
#
# 程序分析：以3月5日為例，應該先把前兩個月的加起來，然後再加上5天即本年的第幾天，特殊情況，閏年且輸入月份大於2時需考慮多加一天：

year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("data error")
sum += day
lead = 0
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    leap = 1
if lead == 1 and month > 2 :
    sum += 1
print("it is the %dth day." % sum)