from rest_framework import serializers

from core.models import Restaurant, Recipe


class RestaurantSerializer(serializers.ModelSerializer):
    """serializers for restaurant object"""

    recipes_avalible = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Recipe.objects.all()
    )

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'user', 'location', 'restaurant_grade')
        read_only_fields = ('id')
