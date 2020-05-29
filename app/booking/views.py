from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
        queryset = self.queryset
        return queryset

    def perform_create(self, serializer):
        """Create a new recipe"""
        return serializer.save(user=self.request.user)
