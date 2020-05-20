from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Restaurant, Recipe

from restaurant import serializers


class RestaurantViewSet(viewsets.ModelViewSet):
    """manage restaturants in db"""
    serializer_class = serializers.RestaurantSerializer
    queryset = Restaurant.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the restaurants for the authenticated user"""
        recipes = self.request.query_params.get('recipes_avalible')
        queryset = self.queryset
        if recipes:
            recipe_ids = self._params_to_ints(recipes)
            queryset = queryset.filter(tags__id__in=recipe_ids)

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.RestaurantDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe"""
        return serializer.save(user=self.request.user)
