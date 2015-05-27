from django.db import models
from django.contrib.auth.models import User
from equipment.models import physiotherapy ,radiotherapy ,ccu,icu,emergency, women_obstetric,\
                                    internal_div,  Orthopedic_surgery_div,child_div,\
                                    Urology_surgery_div, Eye_surgery_div, General_surgery_div, Heart_surgery_div,\
                                     Face_Plastic_surgery_div, Brain_and_Nerve_surgery_div, ENT_surgery_div

USER_CHOICES = (
       (0,'Receptionist'),
       (1,'Boss'),
       (2,'patient'),
       (3,'systemAdmin'),
       (4,'CasualUser'),
       (5,'Pharmacy'),
       (6,'Physician'),
       (7,'Nurse'),

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
class BaseUser(models.Model): #Person
    user_type=models.IntegerField(choices=USER_CHOICES,null=True)
    user=models.OneToOneField(User,primary_key=True,related_name='profile')

    Marital_Status_Choices = (('single', "Single"),
                          ("married", "Married"),
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
    Tel  = models.CharField(max_length=25,null=True,blank=True)
    ssn = models.CharField(max_length=9, unique=True,null=True)
    birthday = models.DateField(null=True,blank=True)
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
    city=models.CharField(max_length=25,null=True,blank=True)
    district=models.CharField(max_length=25,null=True,blank=True)
    street=models.CharField(max_length=30,null=True,blank=True)
    alley=models.CharField(max_length=30,null=True,blank=True)
    building_no = models.CharField(max_length=200,null=True,blank=True)
    postal_code=models.CharField(max_length=30,null=True,blank=True)


    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True,blank=True)
    father_name=models.CharField(max_length='20')

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
          return "%s's profile" % self.user

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#        profile, created = BaseUser.objects.get_or_create(user=instance)
#     post_save.connect(create_user_profile, sender=User)
class Hospital(models.Model,object): #TO DO updating hospital equipment , drugstore ?

   def __init__(self, *args, **kwargs):
      super(Hospital,self).__init__(*args, **kwargs)
      self.__model_label__ = 'hospital'
      self._parent_model = 'hospital'
      self.equipment_labels=list()

   Hospital_ID=models.IntegerField(primary_key=True)
   Hospital_Name=models.CharField(max_length=250)
   Hospital_Type=models.IntegerField(max_length=1,choices=Hospital_Type_CHOICES)

   #hospital equipments attributes & methods
   #units are accessed by their related_name using select_related() method
   physiotherapy=models.OneToOneField(physiotherapy,related_name='physiotherapy',null=True,blank=True)
   radiotherapy=models.OneToOneField(radiotherapy,related_name='radiotherapy',null=True,blank=True)
   ccu=models.OneToOneField(ccu,related_name='ccu',null=True,blank=True)
   icu=models.OneToOneField(icu,related_name='icu',null=True,blank=True)
   internal_div=models.OneToOneField(internal_div,related_name='internal_div',null=True,blank=True)
   child_div=models.OneToOneField(child_div,related_name='child_div',null=True,blank=True)
   emergency=models.OneToOneField(emergency,related_name='emergency',null=True,blank=True)
   women_obstetric=models.OneToOneField(women_obstetric,related_name='women_obstetric',null=True,blank=True)
   Orthopedic_surgery_div=models.OneToOneField(Orthopedic_surgery_div,
                                               related_name='Orthopedic_surgery_div',null=True,blank=True)
   Urology_surgery_div=models.OneToOneField(Urology_surgery_div,related_name='Urology_surgery_div',null=True,blank=True)
   Eye_surgery_div=models.OneToOneField(Eye_surgery_div,related_name='Eye_surgery_div',null=True,blank=True)
   General_surgery_div=models.OneToOneField(General_surgery_div,related_name='General_surgery_div',null=True,blank=True)
   Heart_surgery_div=models.OneToOneField(Heart_surgery_div,related_name='Heart_surgery_div',null=True,blank=True)
   Face_Plastic_surgery_div=models.OneToOneField(Face_Plastic_surgery_div
                                                ,related_name='Face_Plastic_surgery_div',null=True,blank=True)
   Brain_and_Nerve_surgery_div=models.OneToOneField(Brain_and_Nerve_surgery_div,
                                                    related_name='Brain_and_Nerve_surgery_div',null=True,blank=True)
   ENT_surgery_div=models.OneToOneField(ENT_surgery_div,related_name='ENT_surgery_div',null=True,blank=True)
   

   def get_phone_numbers(self):
        try:
            phones=Phone.objects.filter(hospital=self)
        except:
            phones="No Num"
        p=""
        for phone in phones:
            p+="%s | "%str(phone)

        return  p[0:-2]
   @property
   def physiotherapy_object(self):
       try:
           return self.physiotherapy
       except:
           return None
   @property
   def radiotherapy_object(self):
       try:
           return self.radiotherapy
       except:
           return None
   @property
   def ccu_object(self):
       try:
           return self.ccu
       except:
           return None
   @property
   def icu_object(self):
       try:
           return self.icu
       except:
           return None
   @property
   def internal_div_object(self):
       try:
           return self.internal_div
       except:
           return None
   @property
   def child_div_object(self):
       try:
           return self.child_div
       except:
           return None

   @property
   def emergency_object(self):
       try:
           return self.emergency
       except:
           return None
   @property
   def women_obstetric_object(self):
       try:
           return self.women_obstetric
       except:
           return None
   @property
   def Orthopedic_surgery_div_object(self):
       try:
           return self.Orthopedic_surgery_div
       except:
           return None
   @property
   def Urology_surgery_div_object(self):
       try:
           return self.Urology_surgery_div
       except:
           return None
   @property
   def Eye_surgery_div_object(self):
        try:
           return self.Eye_surgery_div
        except:
           return None
   @property
   def General_surgery_div_object(self):
         try:
           return self.General_surgery_div
         except:
           return None
   @property
   def Heart_surgery_div_object(self):
        try:
           return self.Heart_surgery_div
        except:
           return None
   @property
   def Face_Plastic_surgery_div_object(self):
        try:
           return self.Face_Plastic_surgery_div
        except:
           return None
   @property
   def Brain_and_Nerve_surgery_div_object(self):
        try:
           return self.Brain_and_Nerve_surgery_div
        except:
           return None
   @property
   def ENT_surgery_div_object(self):
         try:
           return self.ENT_surgery_div
         except:
           return None

   @property
   def update_equipment_labels(self):
        """ This updates the self.equipments_labels  """
        if self.physiotherapy_object:
            self.equipment_labels+=['physiotherapy']
        if self.radiotherapy_object:
            self.equipment_labels+=["radiotherapy"]
        if self.ccu_object:
            self.equipment_labels+=["ccu"]
        if self.icu_object:
            self.equipment_labels+=["icu"]
        if self.internal_div_object:
            self.equipment_labels+=["internal_div"]
        if self.child_div_object:
            self.equipment_labels+=["child_div"]
        if self.emergency_object:
            self.equipment_labels+=["emergency"]
        if self.women_obstetric_object:
            self.equipment_labels+=["women_obstetric"]

        if self.Orthopedic_surgery_div_object:
            self.equipment_labels+=["Orthopedic_surgery_div"]
        if self.Urology_surgery_div_object:
            self.equipment_labels+=["Urology_surgery_div"]
        if self.Eye_surgery_div_object:
            self.equipment_labels+=["Eye_surgery_div"]
        if self.General_surgery_div_object:
           self.equipment_labels+=["General_surgery_div"]
        if self.Heart_surgery_div_object:
            self.equipment_labels+=["Heart_surgery_div"]
        if self.Face_Plastic_surgery_div_object:
            self.equipment_labels+=["Face_Plastic_surgery_div"]
        if self.Brain_and_Nerve_surgery_div_object:
            self.equipment_labels+=["Brain_and_Nerve_surgery_div"]
        if self.ENT_surgery_div_object:
            self.equipment_labels+=["ENT_surgery_div"]

        return self.equipment_labels


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
    city=models.CharField(max_length=25,null=True,blank=True)
    district=models.CharField(max_length=25,null=True,blank=True)
    street=models.CharField(max_length=30,null=True,blank=True)
    alley=models.CharField(max_length=30,null=True,blank=True)
    building_no = models.CharField(max_length=200,null=True,blank=True)
    postal_code=models.CharField(max_length=30,null=True,blank=True)

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
    photo=models.ImageField(null=True,blank=True,upload_to='images/')
    hospital = models.ForeignKey(Hospital)


    def __unicode__(self):
        return "%s" % self.user.username






