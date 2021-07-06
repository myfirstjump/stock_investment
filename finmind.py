import requests
import pandas as pd
import time

# url = "https://api.finmindtrade.com/api/v4/login"

# parload = {
#     "user_id": "myfirstjump",
#     "password": "a94aa94a",
# }

# data = requests.post(url, data=parload)
# data = data.json()
# print(data)

my_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNC0wOCAyMjo1NToxOSIsInVzZXJfaWQiOiJteWZpcnN0anVtcCIsImlwIjoiMzYuMjI3LjE0NC4yNTAifQ.Rw6QMEW8988_pF7-T_c9HA0cEbtdc3qV-MGkjMzdR0U'
target_number = '3515'
output_folder = "C:\\Datasets\\tw_stock\\info"

# today_date = time.strftime("%Y-%m-%d", time.gmtime()) # 過12點，用倫敦時間。
today_date = time.strftime("%Y-%m-%d") # 沒過12點，用本地時間。

print('\n1. 台股資訊')
'''
台股資訊包含：產業別、股票id、股票名稱、類型(上市Taiwan Stock Exchange(twse)、上櫃Taipei Exchange(tpex))
'''
url = "https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset": "TaiwanStockInfo",
    "token": my_token, # 參考登入，獲取金鑰
}
resp = requests.get(url, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])

data.to_csv(output_folder + '\\TaiwanStockInfo.csv', index=False)

print('\n1.1. 台股類別，可以在多維度圖就不同產業上色來觀察')
stock_types = data['industry_category'].unique()
stock_ids = data['stock_id'].unique()
# print(stock_types)
print('共{}個族群、共{}支股票'.format(len(stock_types), len(stock_ids)))

for each_type in stock_types:
    sub_data = data[data['industry_category']==each_type]
    sub_data_companys = sub_data['stock_name'].unique()
    # print('公司名稱:', sub_data_companys)
    print('產業:{}，此產業包含:{}個公司'.format(each_type, len(sub_data_companys)))

# print('\n2. 個股資訊:', target_number)
# '''
# 重點資訊：Trading_Volume、Trading_Money <-- 此二可推估均價
# spread
# '''

# print('Today date: ', today_date)
# parameter = {
#     "dataset": "TaiwanStockPrice",
#     "data_id": target_number,
#     "start_date": today_date,
#     # "end_date": today_date,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()
# data = pd.DataFrame(data["data"])
# print(data.head())


# print('\n3. 特定日期，每支股票資料')
# '''
# 一次拿特定日期，所有資料(未來將只限贊助會員使用)
# '''


# print('\n4. 即時資料100筆')


# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockPriceTick",
#     "data_id": "2330",
#     "streaming_all_data": True,# 拿取當天所有即時資料
#     "token": my_token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()
# data = pd.DataFrame(data["data"])
# print(data.head())



# print('\n5. 歷史逐筆資料')
# '''
# 台灣股價歷史逐筆資料表 TaiwanStockPriceTick
# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockPriceTick",
#     "data_id": "2330",
#     "start_date": today_date,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()
# data = pd.DataFrame(data["data"])
# print(data.head())



# print('\n5. 即時最佳五檔')
# '''
# 台股即時最佳五檔 TaiwanStockPriceBidAsk
# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockPriceBidAsk",
#     "data_id": target_number,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()["data"]
# if data['date'] == []:
#     data.pop('date', None)
# data = pd.DataFrame(data)
# print(data.head())




# print('\n6. 歷史最佳五檔')
# '''
# 歷史台股最佳五檔 TaiwanStockPriceBidAsk
# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockPriceBidAsk",
#     "data_id": target_number,
#     "start_date": today_date,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()["data"]
# if data['date'] == []:
#     data.pop('date', None)
# data = pd.DataFrame(data)
# print(data)



# print('\n7. PER、PBR資料表')
# '''
# 個股PER、PBR資料表 TaiwanStockPER
# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockPER",
#     "data_id": target_number,
#     "start_date": today_date,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())




# print('\n8. 每5秒委託成交統計 TaiwanStockStatisticsOfOrderBookAndTrade')
# '''
# 每5秒委託成交統計 TaiwanStockStatisticsOfOrderBookAndTrade
# (由於資料量過大，只提供 date 當天 data)
# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockStatisticsOfOrderBookAndTrade",
#     "start_date": today_date,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())



# print('\n9. 加權指數 TaiwanVariousIndicators5Seconds')
# '''
# 加權指數 TaiwanVariousIndicators5Seconds
# 查大盤!!
# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanVariousIndicators5Seconds",
#     "start_date": today_date,
#     "end_date": today_date,
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())





# print('\n10. 當日沖銷交易標的及成交量值 TaiwanStockDayTrading')
# '''
# 當日沖銷交易標的及成交量值 TaiwanStockDayTrading

# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockDayTrading",
#     "data_id": target_number,
#     "start_date": "2020-04-02",
#     "end_date": "2020-04-12",
#     "token": my_token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()
# data = pd.DataFrame(data["data"])
# print(data.head())


# print('\n11. 一次拿特定日期，所有資料(未來將只限贊助會員使用)¶')
# '''
# 一次拿特定日期，所有資料(未來將只限贊助會員使用)¶

# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockDayTrading",
#     "start_date": "2020-04-06",
#     "token": "", # 參考登入，獲取金鑰
# }
# res = requests.get(url, params=parameter)
# temp = res.json()
# data = pd.DataFrame(temp["data"])
# print(data.head())


# print('\n12. 融資融劵表 TaiwanStockMarginPurchaseShortSale')
# '''
# 融資融劵表 TaiwanStockMarginPurchaseShortSale

# '''
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockMarginPurchaseShortSale",
#     "data_id": "2330",
#     "start_date": "2020-04-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())



# print('\n13. 台灣市場整體融資融劵表 TaiwanStockTotalMarginPurchaseShortSale')
# '''
# 台灣市場整體融資融劵表 TaiwanStockTotalMarginPurchaseShortSale

# '''

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockTotalMarginPurchaseShortSale",
#     "start_date": "2020-04-01",
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())







# print('\n14. 法人買賣表 TaiwanStockInstitutionalInvestorsBuySell')
# '''
# 法人買賣表 TaiwanStockInstitutionalInvestorsBuySell

# '''

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockInstitutionalInvestorsBuySell",
#     "data_id": target_number,
#     "start_date": "2020-04-01",
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())



# print('\n15. 台灣市場整體法人買賣表 TaiwanStockTotalInstitutionalInvestors')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockTotalInstitutionalInvestors",
#     "start_date": "2020-04-01",
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())




# print('\n15. 股東結構表 TaiwanStockShareholding')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockShareholding",
#     "data_id": target_number,
#     "start_date": "2020-04-01",
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())



# print('\n16. 股東持股分級表 TaiwanStockHoldingSharesPer¶')
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockHoldingSharesPer",
#     "data_id": "2330",
#     "start_date": "2020-04-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())


# print('\n17. 借券成交明細 TaiwanStockSecuritiesLending')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockSecuritiesLending",
#     "data_id": target_number,
#     "start_date": "2020-04-01",
#     "token": my_token, # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())









# print('=============== 基本面 ===============')

# print('\n18. 綜合損益表 TaiwanStockFinancialStatements')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockFinancialStatements",
#     "data_id": "2330",
#     "start_date": "2019-01-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())


# print('\n19. 資產負債表 TaiwanStockBalanceSheet')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockBalanceSheet",
#     "data_id": "2330",
#     "start_date": "2019-01-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())



# print('\n20. 現金流量表 TaiwanStockCashFlowsStatement')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockCashFlowsStatement",
#     "data_id": "2330",
#     "start_date": "2019-01-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())




# print('\n21. 股利政策表 TaiwanStockDividend')
# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockDividend",
#     "data_id": "2330",
#     "start_date": "2019-01-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())


# print('\n22. 除權除息結果表 TaiwanStockDividendResult')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockDividendResult",
#     "data_id": "2330",
#     "start_date": "2019-01-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())



# print('\n23. 月營收表 TaiwanStockMonthRevenue')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockMonthRevenue",
#     "data_id": "2330",
#     "start_date": "2019-01-01",
#     "token": "", # 參考登入，獲取金鑰
# }
# data = requests.get(url, params=parameter)
# data = data.json()
# data = pd.DataFrame(data['data'])
# print(data.head())
