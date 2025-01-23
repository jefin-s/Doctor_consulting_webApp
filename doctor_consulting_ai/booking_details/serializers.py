from rest_framework import serializers
from booking_details.models import BookingDetails
class android_serializers(serializers.ModelSerializer):
    class Meta:
        model = BookingDetails
        fields = '__all__'
