from rest_framework import serializers
from pmr.models import PatientMedicalReport
class android_serializers(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicalReport
        fields = '__all__'
