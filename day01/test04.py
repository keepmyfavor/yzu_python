import datetime as dt
from dateutil import parser
from dateutil import rrule
from dateutil.relativedelta import relativedelta

buyDate = "2020-11-11"
quitDate = "2021-6-4"

buyDate1 = parser.parse(buyDate)
quitDate1 = parser.parse(quitDate)
# 2020-11-11 00:00:00
print("購買日期為: %s " % buyDate1)
print("離職日期為: %s " % quitDate1)

twoYearDate = buyDate1 + relativedelta(years=2)
# print(twoYearDate)

useDate = (quitDate1 - buyDate1).days
print("使用天數為: %d 天" % useDate)
payDate = (twoYearDate - quitDate1).days
print("支付天數為: %d 天" % payDate)

twoYearDays = (twoYearDate - buyDate1).days
print("二年天數為: %d 天" % twoYearDays)

pyaAmount = 16850 * payDate / twoYearDays
print("扣薪金額為: %d 元" % pyaAmount)
