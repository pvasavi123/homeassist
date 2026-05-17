from rest_framework import serializers
from .models import Booking, BookingItem
from services.serializers import ServiceSerializer
from users.serializers import UserSerializer

class BookingItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookingItem
        fields = ('id', 'service', 'service_id', 'price')

class BookingSerializer(serializers.ModelSerializer):
    items = BookingItemSerializer(many=True)
    customer = UserSerializer(read_only=True)
    worker = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('customer', 'status', 'total_price')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        total_price = sum(item['price'] for item in items_data) # Real app should get price from Service model
        booking = Booking.objects.create(customer=user, total_price=total_price, **validated_data)
        for item_data in items_data:
            BookingItem.objects.create(booking=booking, **item_data)
        return booking
