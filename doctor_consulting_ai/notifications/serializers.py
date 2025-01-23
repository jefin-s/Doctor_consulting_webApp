from rest_framework import  serializers
from notifications.models import Notification
class android_serializers(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'