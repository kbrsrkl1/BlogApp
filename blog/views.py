from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category
# Create your views here.





class CategoryView(ModelViewSet):
    queryset = Category.object.all()
    serializer_class = None