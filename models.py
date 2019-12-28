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

    #def get_absolute_url(self): # As I am using addaminal to add surginfo, this way to reverse a success url doesn't work.
    #    return urls.reverse('index')


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

class TransgenicAnimalLog(models.Model):
    animalid = models.CharField(primary_key=True, max_length=50)
    #cageid = models.CharField(max_length=20)
    dob = models.DateField(blank=True, null=True)
    ear_punch = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    #birth_mate = models.ForeignKey('TransgenicMouseBreeding', models.DO_NOTHING, blank=True, null=True)
    #genotype = models.TextField(blank=True, null=True)
    #test_company = models.CharField(max_length=20, blank=True, null=True)
    #plate_num = models.CharField(max_length=20, blank=True, null=True)
    #full_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'transgenic_animal_log'