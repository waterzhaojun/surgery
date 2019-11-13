from django.db import models

# Create your models here.
class SurgInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
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

