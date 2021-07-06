import sqlite3
import pandas as pd

from py_module.config import Configuration

class DataBase(object):

    def __init__(self):
        self.config_obj = Configuration()

    def insert_one_company_data_flow(self, stock_id, db_name, your_row_data):

        con = sqlite3.connect(db_name)
        

    def build_table_in_db(self, db_name):
        
        data_TaiwanStockInfo = pd.read_csv(self.config_obj.data_TaiwanStockInfo_path, header=0)

        print(data_TaiwanStockInfo.tail(20))
        # stock_id_list = data_TaiwanStockInfo['stock_id'].unique()
        print(data_TaiwanStockInfo[data_TaiwanStockInfo['stock_id']=='Rubber'])
        # print(stock_id_list)



        
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        
        # cur.execute("""SHOW TABLES""")
        cur.execute("""CREATE TABLE IF NOT EXISTS tb1 (
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    price float)""")
        cur.execute("""
                    SELECT name FROM sqlite_master WHERE type='table';
                    """)
        print(cur.fetchall())