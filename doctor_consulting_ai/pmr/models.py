from django.db import models
from patient.models import Patient
from doctor.models import Doctor
# Create your models here.


class PatientMedicalReport(models.Model):
    pmr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    age = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    prescription = models.CharField(max_length=500)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    # patient_id = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'patient_medical_report'

