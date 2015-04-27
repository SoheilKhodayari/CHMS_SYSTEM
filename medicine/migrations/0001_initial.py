# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('code', models.CharField(max_length=50, serialize=False, verbose_name='codigo', primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('description', models.CharField(max_length=350, verbose_name='description', blank=True)),
                ('medicine_type', models.CharField(max_length=350, verbose_name='medicine type', blank=True)),
                ('amount', models.PositiveIntegerField(verbose_name='amount')),
                ('date_produced',models.DateField("Produced Date",blank=True,null=True)),
                ('date_due',models.DateField("Due Date")),
            ],
            options={
                'db_table': 'medicine',
                'verbose_name': 'medicine',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicinePerConsultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(verbose_name='amount')),
                ('medical_consultation', models.ForeignKey(verbose_name='medical consultation', to='consultation.MedicalConsultation')),
                ('medicine', models.ForeignKey(verbose_name='medicine', to='medicine.Medicine')),
            ],
            options={
                'db_table': 'medicine_per_consultation',
                'verbose_name': 'medicine per consultation',
            },
            bases=(models.Model,),
        ),
    ]
