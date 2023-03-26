from rest_framework.viewsets import ModelViewSet


from .models import Category, Blog
from .serializers import BlogSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']
    search_fields =['title', 'content']