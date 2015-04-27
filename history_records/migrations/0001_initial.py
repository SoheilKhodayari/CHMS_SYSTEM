# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ct',
            fields=[
                ('basedocument_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to=b'cts')),
                ('description', models.CharField(max_length=20, choices=[(b'1', b'With injection'), (b'0', b'Without injection')])),
            ],
            options={
            },
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='Ct_area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=100)),
                ('date_of_diagnosis', models.DateField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=None, verbose_name=b'Active?')),
                ('remarks', models.TextField(default=b'None', help_text=b'Any Other Remarks', max_length=1000)),
                ('icd_10', models.CharField(max_length=100, null=True, verbose_name=b'ICD 10', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('had_infectious_disease', models.BooleanField(default=None)),
                ('had_allergic_disease', models.BooleanField(default=None)),
                ('pregnancy_warning', models.BooleanField(default=None)),
                ('patient_current_status', models.TextField(max_length=500, null=True, verbose_name=b'Status', blank=True)),
                ('patient_detail', models.OneToOneField(related_name='history', to='patient.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicationList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medication', models.CharField(help_text=b'Only Generic Names..', max_length=100)),
                ('strength', models.CharField(max_length=100)),
                ('dosage', models.CharField(help_text=b'OD, BD, TDS, QID, HS, SOS, PID etc..', max_length=100)),
                ('prescription_date', models.DateField()),
                ('prescribed_by', models.CharField(default=b'Internal', max_length=100, choices=[(b'internal', b'Internal Doctor'), (b'external', b'External Doctor')])),
                ('currently_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mri',
            fields=[
                ('basedocument_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to=b'mris')),
            ],
            options={
            },
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='Mri_area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_condition_after_surgery', models.TextField(max_length=500, null=True, verbose_name=b'Base Condition', blank=True)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('classification', models.CharField(max_length=200)),
                ('date_of_surgery', models.DateField()),
                ('healed', models.BooleanField(default=None)),
                ('remarks', models.TextField(default=b'None', help_text=b'Any Other Remarks', max_length=1000)),
                ('icd_10', models.CharField(max_length=100, null=True, verbose_name=b'ICD10', blank=True)),
                ('icd_10_pcs', models.CharField(max_length=100, null=True, verbose_name=b'ICD10 PCS', blank=True)),
                ('medical_history', models.ForeignKey(to='history_records.MedicalHistory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('basedocument_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to=b'tests')),
                ('historyFile', models.ForeignKey(related_name='test', to='history_records.MedicalHistory')),
            ],
            options={
            },
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='Test_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('desciption', models.CharField(max_length=100, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='X_ray',
            fields=[
                ('basedocument_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='history_records.BaseDocument')),
                ('image', models.ImageField(upload_to=b'x_rays')),
            ],
            options={
            },
            bases=('history_records.basedocument',),
        ),
        migrations.CreateModel(
            name='X_ray_area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='X_ray_view',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='x_ray',
            name='area',
            field=models.OneToOneField(to='history_records.X_ray_area'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='x_ray',
            name='historyFile',
            field=models.ForeignKey(related_name='x_ray', to='history_records.MedicalHistory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='x_ray',
            name='view',
            field=models.OneToOneField(to='history_records.X_ray_view'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mri',
            name='area',
            field=models.OneToOneField(to='history_records.Mri_area'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mri',
            name='historyFile',
            field=models.ForeignKey(related_name='mri', to='history_records.MedicalHistory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_medication_list',
            field=models.OneToOneField(to='history_records.MedicationList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='medical_history',
            field=models.ForeignKey(to='history_records.MedicalHistory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ct',
            name='area',
            field=models.ForeignKey(to='history_records.Ct_area'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ct',
            name='historyFile',
            field=models.ForeignKey(related_name='ct', to='history_records.MedicalHistory'),
            preserve_default=True,
        ),
    ]
