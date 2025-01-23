from rest_framework import serializers
from ai_solutions.models import AiSolutions
class android_serializers(serializers.ModelSerializer):
    class Meta:
        models=AiSolutions
        fields='__all__'