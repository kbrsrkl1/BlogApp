from rest_framework.viewsets import ModelViewSet


from .models import Category, Blog
from .serializers import BlogSerializer, CategorySerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    