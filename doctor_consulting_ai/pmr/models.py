from django.db import models

# Create your models here.
class PatientMedicalReport(models.Model):
    pmr_id = models.AutoField(primary_key=True)
    pateint_id = models.CharField(max_length=45)
    doctor_id = models.CharField(max_length=45)
    pmr_details = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'patient_medical_report'
