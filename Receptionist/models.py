from django.db import models


from hospital.models import Staff
class Receptionist(Staff):
     def __init__(self, *args, **kwargs):
        super(Receptionist,self).__init__(*args, **kwargs)
        self.__model_label__ = 'Receptionist'
        self._parent_model = 'Staff'

    #define methods here