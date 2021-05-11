from datetime import datetime
import locale

# https://blog.jaycetyle.com/2018/01/python-format-string/
# {:d}        : 整數
# {:f}        : 浮點數
# {:e} {:E}   : 科學記號，例如 1.020000e+01，大小寫就代表 "e" 顯示的大小寫
# {:x} {:X}   : 十六進位，大小寫分別表示 A ~ F 要顯示的大小寫
# {:o}        : 八進位
# {:b}        : 二進位
# {:>}}        : 以百分比的方式輸出


# {:>8d}      : 整數靠右對齊，寬度為 8
# {:^8d}      : 整數置中對齊，寬度為 8
# {:<8d}      : 整數靠右對齊，寬度為 8
# {:8.3f}     : 小數點後保留 3 位，總寬度為 8 (含小數點)
# {:+8.3f}    : 小數點後保留 3 位，帶正負號，總寬度為 8 (含小數點及正負號)

print("{} {} {}".format("A", "B", "C"))  # 不指定位置，依序輸出

print("{2} {0} {1}".format("A", "B", "C"))  # 用數字指定位置

print("{a} {c} {b}".format(a="A", b="B", c="C"))  # 用名稱指定位置

# 前方的數值如基本操作，代表後方參數的位置
# 前面的0和1,代表第幾個變數,ex:123,456
print("|{0:8d}||{1:<8d}|".format(123, 456))

print("|{0:+8.2f}|".format(4.32))

print("|{0:8.2%}|".format(0.8))

# 字串與數值輸出預設對齊方式的比較

print("|{0:8}|".format(123))

print("|{0:8}|".format("abc"))

# 時間表示
# datetime 有實作 format 函數，因此也支援 format 輸出，要再加上 % 格式符，列舉如下
# %a  : 星期縮寫 *　　　　　(Mon)
# %A  : 星期全寫 *　　　　　(Monday)
# %w  : 星期數字  　　　　　(0 … 6)
# %d  : 日期  　　　　　　　(01 … 31)
# %b  : 月份縮寫 *　　　　　(Jan)
# %B  : 月份全寫 *　　　　　(January)
# %m  : 月份數字  　　　　　(01 … 12)
# %y  : 西元年二位數字  　　(00 … 99)
# %Y  : 西元年  　　　　　　(1970 … 2018)
# %H  : 24小時制  　　　　　(00 … 23)
# %I  : 12小時制  　　　　　(01 … 12)
# %p  : AM 或 PM *
# %M  : 分  　　　　　　　　(00 … 59)
# %S  : 秒  　　　　　　　　(00 … 59)
# %f  : 微秒，六位數字  　　(000000 … 999999)
# %c  : 日期和時間 *　　　　(Tue Aug 16 21:30:00 2017)
# %x  : 日期 *　　　　　　　(08/16/2017)
# %X  : 時間 *　　　　　　　(21:30:00)


time = datetime(2021, 5, 11, 14, 30, 30, 123456)
print("{:%Y-%m-%d %H:%M:%S %A}".format(time))

# 注意: locale 和環境相關，如果環境沒有該地區設定，會出現類似以下的錯誤
# locale.Error: unsupported locale setting
locale.setlocale(locale.LC_ALL, "zh_TW.utf8")
print("{:%Y-%m-%d %H:%M:%S %A}".format(time))

site = {"name": "Google", "url": "https://www.google.com"}
print("網站名稱: {name}, 網址: {url}".format(**site))

my_list = ["Google", "https://www.google.com"]
print("網站名稱:{0[0]}, 網址:{0[1]}".format(my_list))  # 0 是必須的
