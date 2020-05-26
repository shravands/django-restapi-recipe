from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register('restaurants', views.RestaurantViewSet)
router.register('reviews', views.ReviewRestaurantViewSet)

app_name = 'restaurant'

urlpatterns = [
    path('', include(router.urls))
]
