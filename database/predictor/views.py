from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PredictorClass(APIView):

    def post(self, request):
        print(request.data)

        """
        The machine learning model will recieve posted data from "request.data".
        Based on that data, the model will predict the chance of heart disease.
        This method will then return the prediction as a response.
        """

        return Response({"result" : "0.5"}, status=status.HTTP_200_OK)
