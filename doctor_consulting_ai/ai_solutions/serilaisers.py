from rest_framework import serializers
from ai_solutions.models import AiSolutions

class android_serializers(serializers.ModelSerializer):
    doctor=serializers.CharField(source='doctor.doctor_name'),
    category=serializers.CharField(source='doctor.departement')
    class Meta:
        model=AiSolutions
        fields=['category','doctor','patient','solutions']