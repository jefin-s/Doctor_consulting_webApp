from django.db import models

# Create your models here.

class AiSolutions(models.Model):
    solution_id = models.AutoField(primary_key=True)
    solutions = models.CharField(max_length=45)
    doctor_id = models.CharField(max_length=45, blank=True, null=True)
    patient_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ai_solutions'
