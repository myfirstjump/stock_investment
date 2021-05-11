import pandas as pd
import requests
import time

from py_module.config import Configuration

class DataBuilder(object):

    def __init__(self):
        self.config_obj = Configuration()

    def read_csv_data(self, data_path):
        
        data = pd.read_csv(data_path, sep=' ', header=None)

        return data

    def get_tw_market_data(self, start_date, end_date):
        '''
        function:
            獲得台股大盤資料
        '''
        parameter = {
            "dataset": "TaiwanVariousIndicators5Seconds",
            "start_date": start_date,
            "end_date": end_date,
            "token": self.config_obj.finmind_token, # 參考登入，獲取金鑰
        }
        data = requests.get(self.config_obj.finmind_data_url, params=parameter)
        data = data.json()
        data = pd.DataFrame(data['data'])
        print(data.tail())
        return data

        

    