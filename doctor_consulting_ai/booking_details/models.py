from django.db import models
from patient.models import Patient
from doctor.models import Doctor
# Create your models here.


class BookingDetails(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    # patient_id = models.IntegerField(blank=True, null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    pmr_id = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'booking_details'
