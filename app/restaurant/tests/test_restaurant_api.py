from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Restaurant, Recipe

from restaurant.serializers import RestaurantSerializer

RESTAURANT_URL = reverse('restaurant:restaurant-list')

def sample_recipe(user, **params):
    """Create and return a sample recipe"""
    defaults = {
        'title': 'default title',
        'time_minutes': 10,
        'price': 5.00
    }
    defaults.update(params)

    return Recipe.objects.create(user=user, **defaults)

class PublicRestaurantApiTest(TestCase):
    """Test the publicly avalible restaurants"""

    def SetUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(RESTAURANT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

