import time
import os 


class Configuration(object):
    
    def __init__(self):

        # self.data_folder = os.path.join("datasets", "Data_2008_PHM")
        # self.file_name = "train.txt"

        # self.features_name = ['unit', 'cycle', 'op_setting_1', 'op_setting_2', 'op_setting_3',] + ['sensor_' + str(i) for i in range(1, 24)]
        # self.features_num = 25

        # self.test_data_folder = os.path.join("datasets", "Data_2008_PHM")
        # self.test_file_name = "final_test.txt"
        self.finmind_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0wNC0wOCAyMjo1NToxOSIsInVzZXJfaWQiOiJteWZpcnN0anVtcCIsImlwIjoiMzYuMjI3LjE0NC4yNTAifQ.Rw6QMEW8988_pF7-T_c9HA0cEbtdc3qV-MGkjMzdR0U"
        self.finmind_data_url = "https://api.finmindtrade.com/api/v4/data"