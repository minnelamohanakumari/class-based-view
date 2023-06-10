from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
class ProductData(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=Productserializer(PQS,many=True)
        return Response(PJD.data)

    def post(self,request):
        PMSO=Productserializer(data=request.data)
        if PMSO.is_valid():
            spo=PMSO.save()
            return Response({'message':'product is created'})
        else:
            return Response({'message':'product is not created'})


    """def put(self,request,productId):
        productobject=Product.objects.get(productId=productId)
        PMSO=Productserializer(data=request.data)
        if PMSO.is_valid():
            spo=PMSO.save()
            return Response({'message':'product is updated'})
        else:
            return Response({'message':'product is failed'})"""


    def put(self,request):
        productId=request.data['productId']
        PO=Product.objects.get(productId=productId)
        UPO=Productserializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product id is updated'})
        else:
            return Response({'message':'product is not updated'})


