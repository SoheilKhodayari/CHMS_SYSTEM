from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

USER_CHOICES = (
       (0,'Paziresh'),
       (1,'Boss'),
       (2,'patient'),
       (3,'systemAdmin'),
       (4,'CasualUser'),

       #TO DO : more/less user choices
   )
Hospital_STAFF_ROLE = (
    ("non_hospital_staff", "Non Hospital Staff"),
    ('secretary', 'Secretary'),
    ('hospital_admin', "Hospital Administrator"),
    ('hospital_staff', "Hospital Staff"),
    ('nurse', "Nurse"),
    ('physio', "Physiotherapist"),
    ("doctor", "Doctor"),
    #TO DO : more/less  choices
)
Hospital_Type_CHOICES=(
       (0,"public"),
       (1,"private")
   )
class BaseUser(models.Model,object):
    def __init__(self,*args,**kwargs):
       super(BaseUser,self).__init__(*args, **kwargs)
       self.__model_label__ = 'BaseUser'
       self._parent_model = 'BaseUser'

    user_type=models.IntegerField(choices=USER_CHOICES,primary_key=True)
    user=models.OneToOneField(User) #getting all attributes of User

class Hospital(models.Model,object): #TO DO updating hospital equipment , drugstore ?

   def __init__(self, *args, **kwargs):
      super(Hospital,self).__init__(*args, **kwargs)
      self.__model_label__ = 'hospital'
      self._parent_model = 'hospital'

   Hospital_ID=models.IntegerField(primary_key=True)
   Hospital_Name=models.CharField(max_length=250)
   Hospital_Type=models.IntegerField(max_length=1,choices=Hospital_Type_CHOICES)

   #TEL,email,website,Address,Fax,Staff are Done by foreignKey

   def __unicode__(self):
        return self.Hospital_Name
   def __repr__(self):
       return str(self)

   def get_users(self,type="p"): # ie: getting patients lists
       user_list=list()
       for user in BaseUser.objects.get(user_type=type):
            user_list+=[user]
       return user_list

class Phone(models.Model):
    def __init__(self, *args, **kwargs):

      super(Phone,self).__init__(*args, **kwargs)
      self.__model_label__ = 'phone'
      self._parent_model = 'hospital'

    area_code    = models.PositiveIntegerField(max_length = 10, default = 21)
    phone_number = models.PositiveIntegerField(max_length=200)

    hospital = models.ForeignKey(Hospital)


    def __unicode__(self):
        return '+98-%s-%s' % ( self.area_code,self.phone_number)

class Email(models.Model):
    def __init__(self, *args, **kwargs):

      super(Email,self).__init__(*args, **kwargs)
      self.__model_label__ = 'email'
      self._parent_model = 'Hospital'


    email_address = models.EmailField(max_length=200)
    hospital = models.ForeignKey(Hospital)

    def __unicode__(self):
        return '%s' % self.email_address

class Website(models.Model):
    def __init__(self, *args, **kwargs):

      super(Website,self).__init__(*args, **kwargs)
      self.__model_label__ = 'website'
      self._parent_model = 'hospital'


    website_address = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital)

    def __unicode__(self):
        return '%s' % self.website_address

class Fax(models.Model):
    def __init__(self, *args, **kwargs):
      super(Fax,self).__init__(*args, **kwargs)
      self.__model_label__ = 'fax'
      self._parent_model = 'Hospital'


    fax_number = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital)


    def __unicode__(self):
        return '%s' % self.fax_number

class Address(models.Model):
    def __init__(self, *args, **kwargs):

      super(Address,self).__init__(*args, **kwargs)
      self.__model_label__ = 'address'
      self._parent_model = 'Hospital'

    country = models.CharField(max_length=200, default = 'Iran')
    city=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    street=models.CharField(max_length=30)
    alley=models.CharField(max_length=30,blank=True)
    building_no = models.CharField(max_length=200)
    postal_code=models.CharField(max_length=30)

    hospital = models.ForeignKey(Hospital)

    def __unicode__(self):
        return '%s - %s, %s\n %s,%s, %s -%s' %(self.country,
                                            self.city,
                                            self.district,
                                            self.street,
                                            self.alley,
                                            self.building_no,
                                            self.postal_code
                                            )

class Staff(BaseUser):

    def __init__(self, *args, **kwargs):
      super(Staff,self).__init__(*args, **kwargs)
      self.__model_label__ = 'staff'
      self._parent_model = 'Hospital'
      if self.user_type ==2:
          raise TypeError("Not Allowed : Staff Must not be a Patient ")

    staff_role = models.CharField("Staff Role",max_length=100,
                                         help_text=" This is the Role of the Staff in the Hospital",
                                         choices=Hospital_STAFF_ROLE)
    is_staff_head = models.BooleanField("Is Staff Head of the Department",default=None)
    hospital = models.ForeignKey(Hospital)


    def __unicode__(self):
        return "%s" % self.user.username





