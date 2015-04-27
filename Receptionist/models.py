from django.db import models
from django.contrib.auth.models import User

from hospital.models import Staff
class Receptionist(Staff):
     def __init__(self, *args, **kwargs):
        super(Receptionist,self).__init__(*args, **kwargs)
        self.__model_label__ = 'Receptionist'
        self._parent_model = 'Staff'
     #user=models.OneToOneField(User,primary_key=True,verbose_name='rec')
    #define methods here