# -*- coding:UTF-8 -*-

account = 10000000  # 帳戶資金
stock = "台積電"  # 標地
price = 590.5  # 成交價
amount = 5432  # 股數
tax_ratio = 1.425/1000  # 證交稅
fee_ratio = 3/1000  # 手續費
# 買入成本
cost = price * amount * (1+tax_ratio)
# 帳戶剩餘資金
account = account - cost
print("成本", cost)  # 預設 sep=" " 預設 end="\n"
print("成本", cost, sep="=", end=".\n")
# %f (浮點數) %d (整數) %s (字串)
print("成本: %.1f" % cost)
# 買進 台積電 5432 股 花費成本 $ 3212166.8 帳戶餘額 $ 6787833.2
print("買進 %s %d 股 花費成本 $%.1f 帳戶餘額 $%.1f" % (stock, amount, cost, account))
print("買進 %s %d 股 花費成本 $%.1f 帳戶餘額 $%s" % (stock, amount, cost, format(account, ",")))
print("買進 %s %d 股 花費成本 $%.1f 帳戶餘額 $%s" % (stock, amount, cost, format(int(account*10)/10, ",")))
