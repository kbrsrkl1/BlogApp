from django.urls import path, include


from .views import CategoryView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('category', CategoryView)


urlpatterns = [
    path('', include(router.urls))
]

