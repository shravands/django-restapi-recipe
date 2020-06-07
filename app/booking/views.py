from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from core.models import Booking

from booking import serializers


class BookingViewSet(viewsets.ModelViewSet):
    """manage restaturants in db"""
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the restaurants for the authenticated user"""
        #queryset = self.queryset.filter(user=self.request.user)
        queryset = self.queryset
        return queryset

    def perform_create(self, serializer):
        """Create a new recipe"""
        return serializer.save(user=self.request.user)

    # def perform_create(self, serializer):
    #     if self.request.method == 'POST':
    #         serialized_data = serializer.data
    #         #serialized_data['test'] = 'test value'
    #         #serialized_data['comments'] = 'comments added from the view class'
    #         #serialized_data['user'] = self.request.user
    #         serialized_data['comments'] = 'comments added from the view class'
    #         serializer.validated_data['comments'] = 'comments added from the view class'

    #         def save(self):
    #             serialized_data['comments'] = 'comments added from the view class'
    #         #return serializer.save(user=self.request.user)
    #         #serializer.validated_data['comments'] = 'comments added from the view class'
    #         raise NotFound(serializer.validated_data)
    #         if serializer.data['seats_number'] == 2:
    #             serializer.data.cust = "customer data"
                
    #         return Response(serializer.data)
    #     return Response({"message": "Hello, world!"})
