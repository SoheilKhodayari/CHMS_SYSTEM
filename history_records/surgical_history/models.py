from django.db import models
from patient.models import Patient

class SurgeryRecord(models.Model):

    """
      This defines the Surgical History that the patient has had
    """

    def __init__(self, *args, **kwargs):
      super(SurgeryRecord,self).__init__(*args, **kwargs)
      self.__model_label__ = "SurgeryRecord"
      self._parent_model = 'patient'


    base_condition_after_surgery = models.TextField("Base Condition",
                                      max_length=500,
                                      null=True,
                                      blank=True
                                      )
    description = models.TextField(max_length=1000,
                                  null=True,
                                  blank=True)
    classification = models.CharField(max_length=200)
    date_of_surgery = models.DateField(auto_now_add=False)

    healed = models.BooleanField(default=None)

    remarks = models.TextField(max_length=1000,help_text="Any Other Remarks",default="None" )

    icd_10 = models.CharField("ICD10", max_length=100, null=True, blank=True)
    icd_10_pcs = models.CharField("ICD10 PCS",max_length=100, null=True, blank=True)

    patient_detail = models.ForeignKey(Patient)


    def __unicode__(self):
        return "%s,%s"%(self.classification,self.icd_10_pcs)

