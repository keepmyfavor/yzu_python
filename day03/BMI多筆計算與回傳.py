# -*- coding:UTF-8 -*-

import math

def getBMI(h, w):
    bmi = w / math.pow(h/100, 2)
    return bmi

def getResult(bmi):
    result = "正常"
    if bmi > 23:
        result = "過重"
    elif bmi < 18:
        result = "過輕"
    return result

def getBMIAndResult(h, w):
    bmi = getBMI(h, w)
    result = getResult(bmi)
    return bmi, result

bmi1 = getBMI(170, 60)
bmi2 = getBMI(180, 90)
print(bmi1, "\n", bmi2)

bmi3, result3 = getBMIAndResult(170, 60)
bmi4, result4 = getBMIAndResult(180, 90)
print(bmi3, result3)
print(bmi4, result4)