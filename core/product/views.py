import pdb
from rest_framework import generics,status
from rest_framework.views import APIView
from .models import Factor, Product
from .serializer import FactorSerializer, ProductSerializer
from .currency_prices import get_currency_prices
from rest_framework.response import Response

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        param = self.request.query_params.get('user', '')
        if param:
            return Product.objects.filter(user=param)

  
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FactorList(generics.ListCreateAPIView):
    serializer_class=FactorSerializer
    

    def get_queryset(self):
        param=self.request.query_params.get('seller','')
        if param:
            return Factor.objects.filter(seller=param)


class FactorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=FactorSerializer
    queryset=Factor.objects.all()



class DailySale(APIView):
    def get(self,request,foramt=None):
        pass


class MonthlySale(APIView):
    def get(self,request,foramat=None):
        pass


class CurrencyInfo(generics.ListAPIView):
    def get(self,request,format=None):
        pdb.set_trace()
        data=get_currency_prices()
        return Response({'cureency':data},status=status.HTTP_200_OK)
