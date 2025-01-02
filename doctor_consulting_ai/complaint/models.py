from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaints = models.CharField(max_length=45)
    complaint_reply = models.CharField(max_length=45)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'
