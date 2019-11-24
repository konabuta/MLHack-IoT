
#Example: scikit-learn and Swagger
import json
import numpy as np
import os
from sklearn.externals import joblib
#import joblib
from sklearn.linear_model import Ridge
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('ssm-test')
    model = joblib.load(model_path)

def run(data):
    input_data = json.loads(data)
    try:
        result = model.predict(input_data['data'][0][0],input_data['data'][1][0])
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
