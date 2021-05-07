
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


while True:
    minPrime = int(input("請輸入一個數字(上限): "))
    if minPrime > 1:
        break
    print("輸入錯誤,請輸入大於 1 的數字")
while True:
    maxPrime = int(input("請輸入一個數字(下限): "))
    if maxPrime > minPrime:
        break
    print("輸入錯誤,請輸入大於 a 的數字")

numPrime = 0
listPrime = []
for n in range(minPrime, maxPrime + 1):
    # i_is_prime = is_prime(n)
    if is_prime(n):
        listPrime.append(n)
        # print(n)
        numPrime += 1

while True:
    selPrime = int(input("請輸入要顯示第幾個質數: "))
    if len(listPrime) >= selPrime > 0:
        break
    elif selPrime <= 0:
        print("輸入錯誤,不得為 0 ")
    elif selPrime > len(listPrime):
        print("超過%d~%d質數的數量, 請重新輸入" % (minPrime, maxPrime))

print(
    "%d ~ %d,總共有 %d 個質數\n%s\n第 %d 個質數為 %d" % (minPrime, maxPrime, numPrime, listPrime, selPrime, listPrime[selPrime - 1]))


