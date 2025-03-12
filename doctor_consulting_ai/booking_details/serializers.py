from rest_framework import serializers
from booking_details.models import BookingDetails
class android_serializers(serializers.ModelSerializer):
    uname=serializers.CharField(source='doctor.doctor_name')
    class Meta:
        model = BookingDetails
        fields = ['uname','booking_id','booking_time','booking_date','status','patient','pmr_id',]
