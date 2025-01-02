from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=45)
    departement = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=450)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'

