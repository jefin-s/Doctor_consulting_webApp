from rest_framework import serializers
from complaint.models import Complaint
class android_serilaizers(serializers.ModelSerializer):
    uname = serializers.CharField(source='doctor.doctor_name')
    class Meta:
        model = Complaint
        fields=['complaint_id ','complaints','complaint_reply','complaint_reply','patient','date','time']


