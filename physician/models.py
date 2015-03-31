from django.db import models
from hospital.models import BaseUser,Hospital
class Physician(BaseUser):
    #Choices
    Marital_Status_Choices = (('single', "Single"),
                          ("married", "Married"),
                          ("divorced", "Divorced"),
                          ('separated', 'Separated'),
                          ('widowed', 'Widowed'),
                          )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    DEGREE_CHOICES = (
        ('DE','dentist'),
        ('GP', 'general practitioner'),
        ('SP', 'Specialist'),
        ('SSP','SSP')
        
    )
    


    
    SPECIALITY_CHOICES = (
            ('cr','cardialogist'), #
            ('dr','dermatologist'), #
            ('en','endocrinologist'), #
            ('ent','ENT (Ear Nose Throat) Specialist'), #
            ('ge','Gerontologist'), #
            ('gy','Gynaecologist'), #
            ('ha','Haematologist'), #
            ('in','Internist'), #
            ('ne','Neurologist'), # 
            ('ob','Obstetrician'), #
            ('on','Oncologist'), #
            ('op','Ophthalmologist'), #
            ('or','Orthodontist'), #
            ('ort','Orthopaedis'), #
            ('pd','Pediatrician'), #
            ('po','Podiatrist'), #
            ('ra','Radiologist'), #
            ('sr','Surgeon'), #
            ('ur','Urologist'), #        
                          
                          )
    

    # below fields are inherited via User
    #username=models.CharField(max_length=50,unique=True,primary_key=True)
    #password=models.CharField(max_length=50)
    #first_name=models.CharField(max_length=50)
    #last_name=models.CharField(max_length=50)
    #email = models.EmailField(max_length=75,blank=True,null=True)



    #More basic Info
    #user_type=
    Tel  = models.CharField(max_length=25)
    ssn = models.CharField(max_length=9, unique=True)
    birthday = models.DateField()
    age = models.CharField(max_length=10, blank=True, null=True)

    #Extra Info
    marital_status = models.CharField(max_length=250,
                                      choices=Marital_Status_Choices,
                                      default="Single",
                                      blank=True,
                                      null=True)

    marital_status_notes = models.CharField(max_length=250,
                                            null=True,
                                            blank=True)

    #Home address
    country = models.CharField(max_length=200, default = 'Iran')
    city=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    street=models.CharField(max_length=30)
    alley=models.CharField(max_length=30,blank=True)
    building_no = models.CharField(max_length=200)
    postal_code=models.CharField(max_length=30)



    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    parent_hospital=models.ForeignKey(Hospital)
    patient_hospital_id = models.CharField('Hospital_ID', max_length=15, unique=True)
    specialty=models.CharField(max_length=3,choices=SPECIALITY_CHOICES)
    graduation_university_name=models.CharField(max_length=200)
    graduation_university_country=models.CharField(max_length=200)
    graduation_university_city=models.CharField(max_length=200)
    degree=models.CharField(max_length=2,choices=DEGREE_CHOICES)
    

    def get_address_as_string(self):
        return '%s - %s, %s\n %s,%s, %s -%s' %(self.country,
                                            self.city,
                                            self.district,
                                            self.street,
                                            self.alley,
                                            self.building_no,
                                            self.postal_code
                                            )
    def __unicode__(self):
        return self.user.username

    
