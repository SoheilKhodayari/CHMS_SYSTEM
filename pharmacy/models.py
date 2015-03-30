from django.db import models
import datetime
from collections import defaultdict as Dict
from hospital.models import Hospital
class Drug(models.Model,object):
    def __init__(self,*args,**kwargs):
       super(Drug,self).__init__(*args, **kwargs)
       self.__model_label__ = 'Drug'
       self._parent_model = 'Pharmacy'

    name=models.CharField("Drug Name",max_length=500)

    description=models.TextField("Drug Description",blank=True,null=True)

    DRUG_TYPE_CHOICES=(
        (0,'Tablet'),
        (1,'Capsule'),
        (2,'Syrup'),
        (3,'Ampoule'),
        (4,'Vial'),
        (5,'Ointment'),
        (6,'Cream'),
        (7,'Lotion'),
        (8,'Gel'),
        (9,'Drop'),
        (10,'Powder & Sachet'),
        (11,'Spray'),
        (12,'Serum')
    )
    drug_type=models.IntegerField(verbose_name="Drug Type",choices=DRUG_TYPE_CHOICES)

    date_produced=models.DateField("Produced Date",blank=True,null=True)
    date_due=models.DateField("Due Date")

    number_available=models.PositiveIntegerField(verbose_name="Available Drug Number",default=0)
    current_pharmacy=models.ForeignKey(Pharmacy)

    def __unicode__(self):
        return "%s"%(self.name)
    def __repr__(self):
        return str(self.name)
    def getType(self):
        return "%s"%self.drug_type

    @property
    def still_can_be_consumed(self):
        if datetime.date.today() > self.date_due :
            return False
        return True

    class Meta:
        model=Drug
        verbose_name="Drug"
        ordering = [ 'name', 'drug_type', 'number_available']
        unique_together=( 'name','drug_type')


class Pharmacy(models.Model,object):
      def __init__(self, *args, **kwargs):
            super(Pharmacy, self).__init__(*args, **kwargs)
            self.__model_label__ = "Pharmacy"
            self._parent_model = 'parent_hospital'

            self.drugs=Dict(lambda : Dict(int)) #self.drugs[drug_name][drug_type]=drug_number
            self.drug_object_list=list()

      designated_hospital=models.OneToOneField(Hospital)

      def createDrug(self,name,drug_type,number,description="",p_date=datetime.date.today()):
          current_pharmacy=self
          today=datetime.date.today()
          due_date=datetime.date(today.year+1,today.month,today.day)
          Drug_Ins = Drug(name=name,drug_type=drug_type,number_available=number,description=description,
                          date_produced=p_date,date_due=due_date,current_pharmacy=current_pharmacy)

          return Drug_Ins


      def add_drug_to_drugs(self,drug_name,drug_type,number):
          """drug is not  in the drugs dict"""
          self.drugs[drug_name][drug_type]=number

          Drug_Ins=self.createDrug(drug_name,drug_type,number)
          self.drugs_object_list+=[Drug_Ins]

      def update_drug(self,drug_name,drug_type,number):
          """drug is already in the drugs dict but the number needs to be updated to number"""
          self.drugs[drug_name][drug_type]=number

          drug=self.createDrug(drug_name,drug_type,number)
          if drug in self.drugs_object_list: #must always Returns true
                self.drugs_object_list[self.drugs_object_list.index(drug)]=number


      def increment_drug(self,drug_name,drug_type,len):
          """drug is already in the drugs dict but the number needs to be incremented by len"""
          self.drugs[drug_name][drug_type]+=len

          for elm in self.drugs_object_list:
              if elm.name==drug_name and elm.drug_type==drug_type:
                  elm.number_available+=len



      def decrement_drug(self,drug_name,drug_type,len):
          """drug is already in the drugs dict but the number needs to be decremented by len"""
          self.drugs[drug_name][drug_type]-=len

          for elm in self.drugs_object_list:
              if elm.name==drug_name and elm.drug_type==drug_type:
                  elm.number_available-=len

      def del_drug(self,drug_name,drug_type):
          #keep track of drug dict
          if len(self.drugs[drug_name])==1:
                del self.drugs[drug_name] #This Deletes the enitre record of drug
          else:
                del self.drugs[drug_name][drug_type]

          #keep track of drug_object_list

          for elm in self.drugs_object_list:
              if elm.name==drug_name and elm.drug_type==drug_type:
                  self.drugs_object_list.remove(elm)

      def is_at_low_number(self,boundary):
          " This returns a dict of warned_drugs with their designated numbers"
          self.drugs_to_be_warned=Dict(lambda : Dict(int))
          for name,values in self.drugs.items() :
              for drug_type,num in values.items():
                    if num<=boundary:
                            self.drugs_to_be_warned[name][drug_type]=self.drugs[name][drug_type]
          return self.drugs_to_be_warned



