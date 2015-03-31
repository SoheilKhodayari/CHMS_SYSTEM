from django.db import models
#TO DO : completing the classes
# Equipment classes are defined here
class physiotherapy(models.Model):
    def __init__(self,*args,**kwargs):
       super(physiotherapy,self).__init__(*args, **kwargs)
       self.__model_label__ = 'physiotherapy'
       self._parent_model = 'Hospital'
class radiotherapy(models.Model):
    def __init__(self,*args,**kwargs):
       super(radiotherapy,self).__init__(*args, **kwargs)
       self.__model_label__ = 'radiotherapy'
       self._parent_model = 'Hospital'
class ccu(models.Model):
    def __init__(self,*args,**kwargs):
       super(ccu,self).__init__(*args, **kwargs)
       self.__model_label__ = 'ccu'
       self._parent_model = 'Hospital'
class icu(models.Model):
    def __init__(self,*args,**kwargs):
       super(icu,self).__init__(*args, **kwargs)
       self.__model_label__ = 'icu'
       self._parent_model = 'Hospital'
class emergency(models.Model):
    def __init__(self,*args,**kwargs):
       super(emergency,self).__init__(*args, **kwargs)
       self.__model_label__ = 'emergency'
       self._parent_model = 'Hospital'
class women_obstetric(models.Model): #Women','NICU
    def __init__(self,*args,**kwargs):
       super(women_obstetric,self).__init__(*args, **kwargs)
       self.__model_label__ = 'women_obstetric'
       self._parent_model = 'Hospital'
class child_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(child_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'child_div'
       self._parent_model = 'Hospital'
class internal_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(internal_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'internal_div'
       self._parent_model = 'Hospital'
class Orthopedic_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(Orthopedic_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Orthopedic_surgery_div'
       self._parent_model = 'Hospital'
class Urology_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(Urology_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Urology_surgery_div'
       self._parent_model = 'Hospital'
class Eye_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(Eye_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Eye_surgery_div'
       self._parent_model = 'Hospital'
class General_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(General_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'General_surgery_div'
       self._parent_model = 'Hospital'
class Heart_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(Heart_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Heart_surgery_div'
       self._parent_model = 'Hospital'
class Face_Plastic_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(Face_Plastic_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Face_Plastic_surgery_div'
       self._parent_model = 'Hospital'
class Brain_and_Nerve_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(Brain_and_Nerve_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Brain_and_Nerve_surgery_div'
       self._parent_model = 'Hospital'
class ENT_surgery_div(models.Model):
    def __init__(self,*args,**kwargs):
       super(ENT_surgery_div,self).__init__(*args, **kwargs)
       self.__model_label__ = 'ENT_surgery_div'
       self._parent_model = 'Hospital'

