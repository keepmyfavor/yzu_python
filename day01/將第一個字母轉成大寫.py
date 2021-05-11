import sys
TT = input("請輸入:")
for x in TT.split():
    print(x[0].upper() + x[1:].lower())
