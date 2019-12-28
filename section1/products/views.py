from django.shortcuts import render
from .models import Products , Manufacturers
from .serializers import manufacturer_serializer , product_serializer
from django.http import JsonResponse 
# Create your views here.

def product_list(request): 
    prod_list =  Products.objects.all()
    prod_data =  product_serializer(prod_list,many=True).data
    return JsonResponse(prod_data, safe= False)

def product_detail(request, pk):
    prod_detail =  Products.objects.get(pk=pk)
    prod_det_data = product_serializer(prod_detail).data
    return JsonResponse(prod_det_data,safe=False)



