from django.db import models
from hospital.models import BaseUser,Hospital
from django.contrib.auth.models import User
class Patient(BaseUser):

    username=models.CharField(max_length=50,unique=True,blank=True)
    firstname=models.CharField(max_length=50,blank=True) # used for searching
    lastname=models.CharField(max_length=50,blank=True)  # used for searching

    parent_hospital=models.ForeignKey(Hospital,null=True,blank=True)
    patient_section=models.CharField("section",max_length=100,null=True,blank=True)
    patient_room=models.CharField("room_num",max_length=100,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.username=self.user.username
        self.firstname=self.user.first_name
        self.lastname=self.user.last_name

        super(Patient, self).save(*args, **kwargs)

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
        return self.user.first_name+" "+self.user.last_name
        # return "Salam"


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
