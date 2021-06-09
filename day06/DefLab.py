#  x 要大於 0 才進行運算
def ctof(c):
    f = c * (9/5) + 32
    return f

def ftoc(f):
    c = (f-32) * (5/9)
    return c

def operator(func, x):
    if x < 500 and x > -500:
        return func(x)
    else:
        return None

c = 10
f = operator(ctof, c)
print("c:", c, "f:", f)

f = 50
c = operator(ftoc, f)
print("f:", f, "c:", c)
