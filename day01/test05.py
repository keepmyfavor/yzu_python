import datetime as dt
from dateutil import parser
from dateutil import rrule
from dateutil.relativedelta import relativedelta
# https://www.pynote.net/archives/1295


def isValidDate(datestr):
    try:
        dt.fromisoformat(datestr)
    except:
        return False
    else:
        return True


buyDate = input("請輸入購買日期: ")
quitDate = input("請輸入離職日期: ")
companyPay = int(input("請輸入補助金額: "))

buyDate = dt.datetime.strptime(buyDate, "%Y-%m-%d").date()
quitDate = dt.datetime.strptime(quitDate, "%Y-%m-%d").date()
useDays = (quitDate - buyDate).days

print("購買日期為: %s " % buyDate)
print("離職日期為: %s " % quitDate)
twoYearDate = buyDate + relativedelta(years=2)

useDate = (quitDate - buyDate).days
print("使用天數為: %d 天" % useDate)
payDate = (twoYearDate - quitDate).days
print("應付天數為: %d 天" % payDate)

twoYearDays = (twoYearDate - buyDate).days
print("二年天數為: %d 天" % twoYearDays)

payAmount = companyPay * payDate / twoYearDays
print("應付金額為: %d 元" % payAmount)
