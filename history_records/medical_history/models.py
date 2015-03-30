from django.db import models
from patient.models import Patient
class MedicationList(models.Model):

    """
    This defines the medication list that the patient has had for that disease

    """
    def __init__(self, *args, **kwargs):
      super(MedicationList,self).__init__(*args, **kwargs)
      self.__model_label__ = "MedicationList"
      self._parent_model = 'patient'

    medication = models.CharField(max_length=100,
                                  help_text="Only Generic Names.."
                                  )
    strength = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100,
                              help_text="OD, BD, TDS, QID, HS, SOS, PID etc.."
                              )
    prescription_date = models.DateField(auto_now_add=False)
    prescribed_by = models.CharField(max_length=100,
                                     choices=(("internal", "Internal Doctor"),
                                              ("external", "External Doctor")
                                                  ),
                                     default = "Internal"
                                     )
    currently_active = models.BooleanField(default=True)



    def __unicode__(self):
        return "%s" % (self.medication)

class Disease(models.Model):
    def __init__(self, *args, **kwargs):
            super(Disease,self).__init__(*args, **kwargs)
            self.__model_label__ = "disease"
            self._parent_model = 'MedicalHistory'

    disease = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    date_of_diagnosis = models.DateField(auto_now_add=False, null=True,blank=True)
    is_active = models.BooleanField("Active?",default=None)
    remarks = models.TextField(max_length=1000,
                               help_text="Any Other Remarks",
                               default="None"
                               )
    #icd 10 is the universal classification of diseases
    icd_10  = models.CharField("ICD 10", max_length=100,null=True, blank=True)

    #medical_History=models.ForeignKey(MedicalHistory)

    disease_medication_list=models.OneToOneField(MedicationList)

class MedicalHistory(models.Model):

    """
      This defines the Medical History that the patient has had .
    """

    def __init__(self, *args, **kwargs):
      super(MedicalHistory,self).__init__(*args, **kwargs)
      self.__model_label__ = "medical_history"
      self._parent_model = 'patient'

    had_infectious_disease = models.BooleanField(default=None)
    had_allergic_disease = models.BooleanField(default = None)
    pregnancy_warning = models.BooleanField(default = None)

    diseases=models.ManyToManyField(Disease) #To add : MedicalHistoryInstance.diseases.add(Disease_Instance)
    patient_detail = models.OneToOneField(Patient) # surgery records are connected accordingly,

    patient_current_status = models.TextField("Status",
                              max_length=500,
                              null=True,
                              blank=True
                              )

    def __unicode__(self):
        return "%s" % (self.patient_detail)


