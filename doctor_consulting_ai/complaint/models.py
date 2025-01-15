from django.db import models
from patient.models import  Patient
from doctor.models import Doctor
# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaints = models.CharField(max_length=45)
    complaint_reply = models.CharField(max_length=45)

    # patient_id = models.IntegerField()

    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'
