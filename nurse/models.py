from django.db import models
from hospital.models import Staff
# Create your models here.
class Nurse(Staff):
    graduation_university_name=models.CharField(max_length=200)
    graduation_university_country=models.CharField(max_length=200)
    graduation_university_city=models.CharField(max_length=200)
    # degree=models.CharField(max_length=2,choices=DEGREE_CHOICES)
    def __unicode__(self):
        return self.user.username