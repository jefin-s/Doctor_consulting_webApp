from rest_framework import serializers
from doctor.models import Doctor

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'