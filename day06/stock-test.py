import requests
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

url = "https://api.finmindtrade.com/api/v3/data"
parameter = {
    "dataset": "Shareholding",
    "stock_id": "2344",
    "date": "2021-05-01",
}
data = requests.get(url, params=parameter)
data = data.json()
data = pd.DataFrame(data['data'])

for i in data.index:
    z = 0
    if i > 0:
        z = data.ForeignInvestmentSharesRatio[i] - data.ForeignInvestmentSharesRatio[i-1]
    print("%s 佔比 %s 增減 %0.2f" % (data.date[i], data.ForeignInvestmentSharesRatio[i], z))




