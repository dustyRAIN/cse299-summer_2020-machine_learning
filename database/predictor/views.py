from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import pandas as pd

class PredictorClass(APIView):

    def post(self, request):
        
        x_value = {}

        x_value['age']      = pd.to_numeric(request.data['age']     , errors='coerce')
        x_value['sex']      = pd.to_numeric(request.data['sex']     , errors='coerce')
        x_value['cp']       = pd.to_numeric(request.data['cp']      , errors='coerce')
        x_value['trestbps'] = pd.to_numeric(request.data['trestbps'], errors='coerce')
        x_value['chol']     = pd.to_numeric(request.data['chol']    , errors='coerce')
        x_value['fbs']      = pd.to_numeric(request.data['fbs']     , errors='coerce')
        x_value['restecg']  = pd.to_numeric(request.data['restecg'] , errors='coerce')
        x_value['thalach']  = pd.to_numeric(request.data['thalach'] , errors='coerce')
        x_value['exang']    = pd.to_numeric(request.data['exang']   , errors='coerce')
        x_value['oldpeak']  = pd.to_numeric(request.data['oldpeak'] , errors='coerce')
        x_value['slope']    = pd.to_numeric(request.data['slope']   , errors='coerce')
        x_value['ca']       = pd.to_numeric(request.data['ca']      , errors='coerce')
        x_value['thal']     = pd.to_numeric(request.data['thal']    , errors='coerce') 
        x_value['thalachcol'] = x_value['thalach'] / x_value['chol']

        testDtaa=pd.DataFrame(x_value, index=[0])

        prediction_model = joblib.load('./models/heart_disease_predictor_model_001.pkl')
        pipeline = joblib.load('./models/classifier_pipeline.pkl')

        processed_values = pipeline.transform(testDtaa)
        result = prediction_model.predict(processed_values)

        print(result[0])

        return Response({"result" : result[0]}, status=status.HTTP_200_OK)
