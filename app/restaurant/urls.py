from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register('recipes', views.RestaurantViewSet)

app_name = 'restaurant'

urlpatterns = [
    path('', include(router.urls))
]
