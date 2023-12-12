import sys
import os
import dill
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from src_ene.exception import CustomException

def save_object(file_path, object):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'w') as file_obj:
            dill.dumps(object,file_obj)

    except Exception as e:
        raise CustomException(e,sys)


def evaluate_model_report(X_train, y_train,X_test,y_test,models):
    try:
        report=[]


        for i in range(len(models)):
            model=list(models.values())[i]

            model.fit(X_train,y_train) #train model

            y_train_pred=model.predict(X_test)

            y_test_pred=model.predict(y_test)

            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report





    except  Exception as e:

        raise CustomException(e,sys)

