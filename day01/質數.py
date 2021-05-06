def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    while True:
        minPrime = int(input("請輸入最小值: "))
        maxPrime = int(input("請輸入最大值: "))
        selPrime = int(input("顯示第幾個值: "))
        if minPrime > 1 and minPrime < maxPrime:
            numPrime = 0
            listPrime = []
            for n in range(minPrime, maxPrime + 1):
                # i_is_prime = is_prime(n)
                if is_prime(n):
                    listPrime.append(n)
                    # print(n)
                    numPrime += 1
            if len(listPrime) < selPrime:
                print("輸入要顯示的值太大, 請重新輸入")
                main()
            print("%d到%d,總共有%d個質數\n%s\n第%d個質數為%d" % (minPrime, maxPrime, numPrime, listPrime, selPrime, listPrime[selPrime - 1]))
            break
        else:
            print("最小值不能小於1,最大值要大於最小值, 請重新輸入")


main()
