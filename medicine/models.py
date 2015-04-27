from django.db import models
from django.utils.translation import ugettext_lazy as _

class Medicine(models.Model):
    def __init__(self,*args,**kwargs):
        super(Medicine,self).__init__(*args, **kwargs)
        self.__model_label__ = 'Medicine'
        self._parent_model = 'Pharmacy'

    DRUG_TYPE_CHOICES=(('Tablet','Tablet'),
        ('Capsule','Capsule'),
        ('Syrup','Syrup'),
        ('Ampoule','Ampoule'),
        ('Vial','Vial'),
        ('Ointment','Ointment'),
        ('Cream','Cream'),
        ('Lotion','Lotion'),
        ('Gel','Gel'),
        ('Drop','Drop'),
        ('Powder & Sachet','Powder & Sachet'),
        ('Spray','Spray'), ('Serum','Serum')
                         )
    code = models.CharField(
        max_length=50,
        primary_key=True,
        verbose_name=_('codigo'),
    )
    name = models.CharField(
        max_length=250,
        verbose_name=_('name'),
    )
    description = models.CharField(
        max_length=350,
        blank=True,
        verbose_name=_('description'),
    )
    medicine_type = models.CharField(choices=DRUG_TYPE_CHOICES,
        max_length=350,
        blank=True,
        verbose_name=_('medicine type'),
    )
    amount = models.PositiveIntegerField(
        verbose_name=_('amount'),
    )

    date_produced=models.DateField("Produced Date",blank=True,null=True)
    due_date=models.DateField("Due Date")




    def __unicode__(self):
        return unicode(self.code)
    def __repr__(self):
        return str(self.name)

    class Meta:
        db_table = 'medicine'
        verbose_name = _('medicine')

