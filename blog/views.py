from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Blog
from .serializers import BlogSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class =  [IsAdminOrReadOnly]
    filterset_fields = ['name']


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']
    search_fields =['title', 'content']