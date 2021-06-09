def get_sum(*scroe):   # 數組
    print(type(scroe), scroe, len(scroe))
    return sum(scroe)


print(get_sum(10, 20, 30))
print(get_sum(10))
print(get_sum())
print(get_sum(10, 3.14))
