from rest_framework import serializers
from django.db.models import Avg

from core.models import Restaurant, Recipe, ReviewRestaurant

from recipe.serializers import RecipeDetailSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    """serializers for restaurant object"""
    recipes_avalible = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Recipe.objects.all()
    )

    avg_restaurant_rating = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'space_valible', 'rating', 'email_contact','location', 'restaurant_grade', 'recipes_avalible', 'avg_restaurant_rating')
        read_only_fields = ('id',)

    def get_avg_restaurant_rating(self, restaurant):
        if restaurant:
            queryset = ReviewRestaurant.objects.filter(restaurant_id=restaurant.id).aggregate(Avg('rating'))
            #return ("we are bale to get values")
            return queryset['rating__avg'] # getting the avg restaurant reviews based on the restaurant only
        else:
            return("not getting any values")


class ReviewRestaurantSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Recipe.objects.all()
    )

    restaurant = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Restaurant.objects.all()
    )

    class Meta:
        model = ReviewRestaurant
        fields = ('id', 'user', 'recipe', 'restaurant', 'rating', 'comments')
        read_only_fields = ('id',)


class ReviewRestaurantDetailSerializer(serializers.ModelSerializer):
    # using the RecipeDetailSerializer to get the detailed view for tags and ingridents
    restaurant = RestaurantSerializer(read_only=True)
    recipe = RecipeDetailSerializer(read_only=True)

    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = ReviewRestaurant
        fields = ('id', 'user', 'recipe', 'restaurant', 'rating', 'comments', 'average_rating')
        read_only_fields = ('id',)

    def get_average_rating(self, reviewrestaurant):
        if reviewrestaurant:
            queryset = ReviewRestaurant.objects.filter(restaurant_id=reviewrestaurant.restaurant.id, recipe_id=reviewrestaurant.recipe.id).aggregate(Avg('rating'))
            #return (reviewrestaurant.recipe.id)
            return queryset['rating__avg'] #the data will be recieved in the form of dictonary for the queryset
        else:
            return ("unable to get average_rating for the restaurant")

class RestaurantDetailSerializer(RestaurantSerializer):
    """serialize the restaurant detail"""
    # using the RecipeDetailSerializer to get the detailed view for tags and ingridents
    recipes_avalible = RecipeDetailSerializer(many=True, read_only=True)
    