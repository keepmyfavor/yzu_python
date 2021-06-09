def ftoc(F):
    C = (F - 32) * 5 / 9
    return C

def ctof(C):
    F = C * (9 / 5) + 32
    return F

print("34F = %0.1f C" % ftoc(34))
print("38C = %0.1f F" % ctof(38))
