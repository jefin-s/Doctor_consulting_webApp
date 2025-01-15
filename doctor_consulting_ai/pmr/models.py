from django.db import models
from patient.models import Patient
from doctor.models import Doctor
# Create your models here.

class PatientMedicalReport(models.Model):
    pmr_id = models.AutoField(primary_key=True)
    pmr_details = models.CharField(max_length=500)
    # patient_id = models.IntegerField(blank=True, null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    # doctor_id = models.IntegerField(blank=True, null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'patient_medical_report'
