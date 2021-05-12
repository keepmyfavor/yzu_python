# 某公司有18位員工，其中10位在去年投資股票，一年的獲
# 利率如下(單位：%)：
# 7.6 3.9 15.6 28.3 1.2 10.8 35.3 45.6 10.2 0.5
# 另外8位員工投資買公債一年內獲利率如下(單位：%)
# 6.8 7.2 6.8 7.5 6.9 7.9 7.9 7.1 7.2
# 試分別求此公司的員工投資股票與公債的獲利率變異係數。
#
# 解答：投資股票的獲利率變異係數 C.V. = 0.969
# 投資買公債的獲利率變異係數 C.V. = 0.059
import statistics as stat
import matplotlib.pyplot as plt
import matplotlib as mpl

stock = [7.6, 3.9, 15.6, 28.3, 1.2, 10.8, 35.3, 45.6, 10.2, 0.5]
bond = [6.8, 7.2, 6.8, 7.5, 6.9, 7.9, 7.9, 7.1, 7.2]

stock_cv = stat.stdev(stock)/stat.mean(stock)
bond_cv = stat.stdev(bond)/stat.mean(bond)

print("股票 cv:", "%.2f%%" % (stock_cv*100))
print("公債 cv:", "%.2f%%" % (bond_cv*100))

font = mpl.font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc")
plt.plot(stock, marker="o", color=(255/255, 0/255, 0/255))
plt.plot(bond, marker="o", color=(0/255, 0/255, 255/255))
plt.ylabel("獲利", fontproperties=font)
plt.grid(True)
plt.title("股票公債獲利表", fontproperties=font)
plt.show()
