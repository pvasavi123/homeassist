from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'WORKER':
            return Booking.objects.filter(worker=user)
        elif user.role == 'ADMIN':
            return Booking.objects.all()
        return Booking.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save()
