from django.db import models
from hospital.models import BaseUser,Hospital
class Patient(BaseUser):
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

    # below fields are inherited via User
    #username=models.CharField(max_length=50,unique=True,primary_key=True)
    #password=models.CharField(max_length=50)
    #first_name=models.CharField(max_length=50)
    #last_name=models.CharField(max_length=50)
    #email = models.EmailField(max_length=75,blank=True,null=True)



    #More basic Info
    user_type=2
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

    occupation = models.CharField(max_length=100,blank=True,null=True)
    occupation_notes = models.CharField(max_length=100,
                                        null=True,
                                        blank=True
                                        )

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

    #To Do : complete patient detail,methods

class Guardian(models.Model):

    """
      Class that defines the Guardian of a Particular patient.
    """

    def __init__(self, *args, **kwargs):
      super(Guardian,self).__init__(*args, **kwargs)
      self.__model_label__ = "Guardian"
      self._parent_model = 'patient'

    guardian_name = models.CharField(max_length=20, blank=True,
                                     null=True,
                                     help_text="Enter Guardian Name if Patient is a minor"
                                     )
    relation_to_guardian = models.CharField('Relation',
                                            max_length=20,
                                            blank=True,
                                            null=True,
                                            help_text="Enter relationship to Guardian if Patient is a Minor",
                                            )
    guardian_phone = models.PositiveIntegerField('Phone',
                                                 max_length=20,
                                                 blank=True,
                                                 null=True
                                                 )
    patient_detail = models.ForeignKey(
        Patient, null=True, blank=True)

    def __unicode__(self):
        if self.guardian_name:
            return "%s " % (self.guardian_name)
        else:
            return "No Guardian Name Provided"
