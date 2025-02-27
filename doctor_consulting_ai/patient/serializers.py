from rest_framework import serializers
from patient.models import Patient
class android_seriliazers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields='__all__'