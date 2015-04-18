from django.db import models
from hospital.models import BaseUser,Hospital
class Patient(BaseUser):


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
