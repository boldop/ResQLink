from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import *

# Create your views here.
class AllProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class createProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class updatedeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class AllCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class createCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class updatedeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

