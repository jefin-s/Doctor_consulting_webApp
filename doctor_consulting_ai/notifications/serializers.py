from rest_framework import  serializers
from notifications.models import Notification
class android_serializers(serializers.ModelSerializer):
    uname = serializers.CharField(source='doctor.doctor_name')
    class Meta:
        model=Notification
        fields=['uname','notification_id','notification_name','date','time']