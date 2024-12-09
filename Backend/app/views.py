from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import *

# Create your views here.
class AllProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class AllCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
