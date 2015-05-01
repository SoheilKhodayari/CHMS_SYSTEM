from django.db import models

from patient.models import Patient

class schedule(models.Model):
    patient=models.ForeignKey(Patient,primary_key=True)
    event_date=models.DateTimeField(auto_now_add=True)
    event=models.CharField(max_length=400)
    event_time=models.TimeField(auto_now_add=True)
    related_division=models.CharField(max_length=200)
    description=models.CharField(max_length=500)

    class Meta:
        unique_together =('event_date','event_time')