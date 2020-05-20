from rest_framework import serializers

from core.models import Restaurant, Recipe

from recipe.serializers import RecipeDetailSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    """serializers for restaurant object"""

    recipes_avalible = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Recipe.objects.all()
    )

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'space_valible', 'rating', 'email_contact','location', 'restaurant_grade', 'recipes_avalible')
        read_only_fields = ('id',)


class RestaurantDetailSerializer(RestaurantSerializer):
    """serialize the restaurant detail"""
    # usung the RecipeDetailSerializer to get the detailed view for tags and ingridents
    recipes_avalible = RecipeDetailSerializer(many=True, read_only=True)
