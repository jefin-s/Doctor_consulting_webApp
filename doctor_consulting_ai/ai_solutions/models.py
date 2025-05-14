from django.db import models
from doctor.models import Doctor
from patient.models import Patient
# Create your models here.

class AiSolutions(models.Model):
    solution_id = models.AutoField(primary_key=True)
    solutions = models.CharField(max_length=45)
    # doctor_id = models.IntegerField(blank=True, null=True)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # patient_id = models.IntegerField(blank=True, null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ai_solutions'

