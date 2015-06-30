from django.db import models
from collections import defaultdict as Dict
from hospital.models import Hospital,BaseUser
from django.contrib.auth.models import User
import datetime

class Pharmacy(models.Model,object):
      def __init__(self, *args, **kwargs):
            super(Pharmacy, self).__init__(*args, **kwargs)
            self.__model_label__ = "Pharmacy"
            self._parent_model = 'parent_hospital'

            #self.drugs=Dict(lambda : Dict(int)) #self.drugs[drug_name][drug_type]=drug_number
            self.drugs=Dict() # self.drugs[drug_code]=drug_num
            self.drug_object_list=list()
            self.user_type=5

      designated_hospital=models.OneToOneField(Hospital,null=True,blank=True)

class Pharmacy_Undertaker(BaseUser):
      def __init__(self, *args, **kwargs):
            super(Pharmacy_Undertaker, self).__init__(*args, **kwargs)
            self.__model_label__ = "Pharmacy_Undertaker"
            self._parent_model = 'Pharmacy'
            self.user_type=5
      Pharmacy=models.OneToOneField(Pharmacy,primary_key=True)




