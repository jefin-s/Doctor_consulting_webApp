# Generated by Django 3.2.25 on 2025-01-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedicalReport',
            fields=[
                ('pmr_id', models.AutoField(primary_key=True, serialize=False)),
                ('pmr_details', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'patient_medical_report',
                'managed': False,
            },
        ),
    ]
