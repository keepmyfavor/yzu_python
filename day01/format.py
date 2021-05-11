# print(f'{input()} and {input()} sitting in the tree')

# name = "fred"
# print(f"he said his name is {name}.")

# print(f"he said his name is {input()}.")

# print(f'{input()} and {input()} sitting in the tree')
# print("%s and %s sitting in the tree" % ({input()}, {input()}))
# print("%s and %s sitting in the tree" % (input(), input()))

# print("{1} {0} sitting in the tree".format(input(), input()))
print("{} and {} sitting in the tree".format(input(), input()))
print(f'{input()} and {input()} sitting in the tree')

a = 2
b = 3
print("%d/%d = %f" % (a, b, float(a/b)))  # %-formatting
print("{a}/{b} = {c}".format(a=a, b=b, c=float(a/b)))  # str-format
print(f"{a}/{b} = {float(a/b)}")  # f-string

print("{} {} {}".format("A", "B", "C"))  # 不指定位置，依序輸出
print("{2} {0} {1}".format("A", "B", "C"))  # 用數字指定位置
print("{a} {c} {b}".format(a="A", b="B", c="C"))  # 用名稱指定位置

