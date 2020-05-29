from rest_framework import serializers
from core.models import Booking, Restaurant

from restaurant.serializers import RestaurantSerializer


class BookingSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Restaurant.objects.all()
    )

    class Meta:
        model = Booking
        fields = ('id', 'user', 'restaurant', 'seats_number', 'time_start', 'time_end', 'comments')
        read_only_fields = ('id', 'user',)
