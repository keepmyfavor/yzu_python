# -*- coding:UTF-8 -*-

def getChickenAndRabbit(sum, feet):
    '''
    :param sum: 83
    :param feet:  240
    :return:

    rabbit = (240 - 83 * 2) / 2
    chicken = 83 - rabbit
    return chicken, rabbit
    '''

    if feet/4 <= sum <= feet/2:
        rabbit = (feet - sum * 2) / 2
        chicken = sum - rabbit
        return chicken, rabbit
    else:
        print("無法計算")
        return 0, 0

print(getChickenAndRabbit(83, 240))

c, r = getChickenAndRabbit(150, 240)
print(c, r)