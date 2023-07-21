import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngesionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngesion:
    def __init__(self):
        self.ingesion_config=DataIngesionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingesion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Exported/Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingesion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingesion_config.raw_data_path,index=False,header=True)

            logging.info("Train/Test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=40)

            train_set.to_csv(self.ingesion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingesion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingesion_config.train_data_path,
                self.ingesion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngesion()
    obj.initiate_data_ingestion()

            

    