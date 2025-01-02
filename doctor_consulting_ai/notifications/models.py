from django.db import models

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification_name = models.CharField(max_length=45)
    doctor_id = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'
        unique_together = (('notification_id', 'notification_name'),)

