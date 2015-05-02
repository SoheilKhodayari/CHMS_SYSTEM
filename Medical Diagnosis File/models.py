__author__ = 'soheil'
from history_records.models import Disease
from django.db import models
class MedicalFile(models.Model):

    """
    This defines current patient file at hospital

    """
    def __init__(self, *args, **kwargs):
      super(MedicalFile,self).__init__(*args, **kwargs)
      self.__model_label__ = "MedicalFile"
      self._parent_model = 'Patient'

    Diagnosed_Disease=models.OneToOneField(Disease) # medication list accessed by Disease.medication list
    Doc_name=models.CharField(max_length=50) # Doc=models.OneToOneField(physician)
