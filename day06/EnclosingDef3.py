# 嵌套函式 III

def make_lotto(n):
    def muli(x):
        return n * x
    return muli

m3 = make_lotto(3)  # n = 3
m5 = make_lotto(5)  # n = 5

print(m3(6))  # x = 6
print(m5(7))  # x = 7

print(m3(m5(2)))
print(m3(10))

def outer():
    x = 10
    def inner():
        print((x))
    x = 20
    return inner


f = outer()
f()