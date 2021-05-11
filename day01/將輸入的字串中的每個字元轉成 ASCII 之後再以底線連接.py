s = input("請輸入一個字串")
a = []
for x in range(len(s)):

    a.append(str(ord(s[x])))

b = '_'.join(a)

print(b)

# >>>ord('a')
# 97
# >>> ord('b')
# 98
# >>> ord('c')
# 99
