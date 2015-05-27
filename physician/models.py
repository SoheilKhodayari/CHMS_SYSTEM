from django.db import models
from hospital.models import Staff,Hospital

class Physician(Staff):

    DEGREE_CHOICES = (
        ('DE','dentist'),
        ('GP', 'general practitioner'),
        ('SP', 'Specialist'),
        ('SSP','SSP')
        
    )
    SPECIALITY_CHOICES = (
            ('cr','cardialogist'), 
            ('dr','dermatologist'), 
            ('en','endocrinologist'), 
            ('ent','ENT (Ear Nose Throat) Specialist'), 
            ('ge','Gerontologist'), 
            ('gy','Gynaecologist'), 
            ('ha','Haematologist'), 
            ('in','Internist'), 
            ('ne','Neurologist'),  
            ('ob','Obstetrician'), 
            ('on','Oncologist'), 
            ('op','Ophthalmologist'), 
            ('or','Orthodontist'), 
            ('ort','Orthopaedis'), 
            ('pd','Pediatrician'), 
            ('po','Podiatrist'), 
            ('ra','Radiologist'), 
            ('sr','Surgeon'), 
            ('ur','Urologist'),        
                          )

    specialty=models.CharField(max_length=3,choices=SPECIALITY_CHOICES)
    graduation_university_name=models.CharField(max_length=200,null=True,blank=True)
    graduation_university_country=models.CharField(max_length=200,null=True,blank=True)
    graduation_university_city=models.CharField(max_length=200,null=True,blank=True)
    degree=models.CharField(max_length=2,choices=DEGREE_CHOICES)
    

    def __unicode__(self):
        return self.user.username

    
