from rest_framework import serializers
from core.models import Booking, Restaurant

from django.db.models import Sum

from restaurant.serializers import RestaurantSerializer

# this is an example for modifying the serializer data

class BookingSerializer(serializers.ModelSerializer):

    restaurant = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Restaurant.objects.all()
    )

    class Meta:
        model = Booking
        fields = ('id', 'user', 'restaurant', 'seats_number', 'time_start', 'time_end', 'comments')
        read_only_fields = ('id', 'user',)

    # creating the global id for the restaurant from the data field to accessible else where in the serializer

    def validate_restaurant(self, restaurant):
        global restaurnat_id
        restaurnat_id = restaurant.id
        return restaurant

    # checking the the avalible seating data from the restaurants and booking objects
    def validate(self, data):

        # change in the custom value of the comments
        #data['comments'] = 'the comments added from the serializers, {}'.format(data['seats_number'])
        # Adding the validation for time constrain
        time_diff = (data['time_end'] - data['time_start']).seconds/60
        if time_diff > 120:
            raise serializers.ValidationError("The restaurant cannot be booked for more than 2 hours")

        # data validation for the seating numbers based on seating avalible in the restaurant
        booked_seats = Booking.objects.filter(restaurant_id=restaurnat_id, is_active=True).aggregate(Sum('seats_number'))
        avalible_seats = Restaurant.objects.filter(id=restaurnat_id).values('total_seating')
        avalible_seats_total = avalible_seats[0]['total_seating']
        already_booked = booked_seats['seats_number__sum']

        # the condition is added to rectify if there are no entries for a particular restaurant
        if already_booked is None:
            already_booked = 0
        seats_avalible_now = int(avalible_seats_total) - int(already_booked)
        if data['seats_number'] >= 10:
            raise serializers.ValidationError("The seats cant be more than 10, seats avalible are:".format(seats_avalible_now))
        elif seats_avalible_now <= 0:
            raise serializers.ValidationError("The restaurant is completly full")
        elif (seats_avalible_now - data['seats_number']) < 0 :
            raise serializers.ValidationError(" Only {} seats are avalible for booking".format(seats_avalible_now))
        return data
