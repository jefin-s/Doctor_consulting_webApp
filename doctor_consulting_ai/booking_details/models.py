from django.db import models

# Create your models here.


class BookingDetails(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    doctor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking_details'

