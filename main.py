
import os

from py_module.config import Configuration
from py_module.data_builder import DataBuilder
from py_module.database import DataBase
# from py_module.data_preprocessing import DataProprocessing
# from py_module.data_exploration import DataExploration
# from py_module.learning_definition import LearningDefinition
# from py_module.data_training import DataTraining
# from py_module.plot_module import PlotDesign
# from py_module.data_evaluation import DataEvaluation
# from py_module.data_training_tf18 import DataTrainingTF18

'''
台股資金流預測模型

data：
    -. x1 ~ x48
        各族群平均資金漲跌

        ['ETF' '上櫃指數股票型基金(ETF)' '指數投資證券(ETN)' '水泥工業' '其他' '食品工業' '電器電纜' '農業科技業'
        '觀光事業' '塑膠工業' '建材營造' '汽車工業' '電子零組件類' '紡織纖維' '貿易百貨' '電子工業' '電子零組件業' '電機機械'
        '生技醫療類' '電腦及週邊類' '化學生技醫療' '生技醫療業' '化學工業' '其他電子類' '玻璃陶瓷' '造紙工業' '鋼鐵工業'
        '橡膠工業' '航運業' '電腦及週邊設備業' '半導體業' '其他電子業' '通信網路業' '光電業' '電子通路業' '資訊服務業'
        '油電燃氣業' '金融保險' '文化創意業' '光電業類' '半導體類' '通信網路類' '電子商務業' '資訊服務類' '電子通路類'
        '金融業' '油電燃氣類' '存託憑證']
    
    -. 
output：
    -. y1 ~ y48 下個月的平均漲幅值
'''


class StockTrendPrediction(object):

    """
    Main Flow:
    1. data building
    2. data preprocessing
    3. data training
    4. data evaluating
    """

    def __init__(self):
        self.config_obj = Configuration()
        self.data_obj = DataBuilder()
        self.db_obj = DataBase()
        # self.data_preprocessing_obj = DataProprocessing()
        # self.learning_define_obj = LearningDefinition()
        # self.data_exploration_obj = DataExploration()
        # self.learing_def_obj = LearningDefinition()
        # self.training_obj = DataTraining()
        # self.plotting_obj = PlotDesign()
        # self.evaluation_obj = DataEvaluation()
        # self.training_tf18_obj = DataTrainingTF18()

    def data_building(self):
    
        # data = self.data_obj.get_tw_market_data('2005-01-11', '2005-01-11')
        self.db_obj.build_table_in_db('my_db')
        

    # def data_exploration(self, data):

    #     # self.data_exploration_obj.data_exploration_2008_PHM_Engine_data(data)

    # def data_preprocessing(self, data):
        
    #     # data = self.data_preprocessing_obj.data_preprocessing_2008_PHM_Engine_data(data, self.config_obj.features_name)
    #     # data = self.data_preprocessing_obj.features_standardization(data, self.config_obj.standardization_features)

    #     # return data
    
    # def learning_define(self, data):
        
    #     ### PHM 2008 Engine, 

    #     # new_data = self.learning_def_obj.learning_define_2008_PHM_Engine_data(data)        

    #     # return new_data

    # def model_training(self, data):

    # #     my_history = self.training_obj.training_2008_PHM_Engine_data(data, epochs=30, load_model = False)
    # # #     hyperparameters = {'batch_szie':[8,16,32,64, 128], "epochs":[10, 30, 50, 100, 200, 300], }
    # # #     self.training_obj.grid_search_with_cross_validation(hyperparameters, "data", "cv_fold", "preprocessing_function", "training_function", "scoring_metric")
        
    # #     return my_history

    # def plotting_function(self, obj):

    #     # self.plotting_obj.learning_curve(obj)

    # def data_evaluation(self, test_data):
        
    #     self.evaluation_obj.data_evaluation_2008_PHM_Engine_data(test_data)

    # def data_training_tf18(self, data):

    #     self.training_tf18_obj.training_PHM_2008_Engine_data(data, model_string="RNN")



def main_flow():
    
    main_obj = StockTrendPrediction()
    
    main_obj.data_building()
    # data = main_obj.data_preprocessing(data)
    # testing_data = main_obj.data_preprocessing(testing_data)
    # # main_obj.data_exploration(data)
    # print(data)
    # # Training
    # my_history = main_obj.model_training(data)
    # main_obj.plotting_function(my_history)

    # ### Evaluation
    # # while(True):
    # #     main_obj.data_evaluation(testing_data)
    # main_obj.data_evaluation(testing_data)

    ### Code Test
    # main_obj.data_training_tf18(data)


if __name__ == "__main__":
    main_flow()