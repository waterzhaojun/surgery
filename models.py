from django.db import models
from django.contrib.postgres.fields import JSONField
import django.urls as urls

# Create your models here.
class SurgInfo(models.Model):
    animalid = models.CharField(primary_key=True, max_length=50)
    species = models.CharField(max_length=10)
    strain = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=1)
    transgenic_id = models.CharField(max_length=50, blank=True, null=True)
    terminated = models.BooleanField()
    note = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    ear_punch = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surg_info'


class SurgTreatment(models.Model):
    animalid = models.ForeignKey(SurgInfo, models.DO_NOTHING, db_column='animalid')
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    method = models.CharField(max_length=20)
    operator = models.CharField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parameters = JSONField()  # This field type is a guess.
    serialid = models.AutoField(primary_key=True) # There is a warning that can't have two AutoField. So I disable this one.

    class Meta:
        managed = False
        db_table = 'surg_treatment'
