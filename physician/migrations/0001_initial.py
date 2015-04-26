# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('staff_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hospital.Staff')),
                ('patient_hospital_id', models.CharField(unique=True, max_length=15, verbose_name=b'Hospital_ID')),
                ('specialty', models.CharField(max_length=3, choices=[(b'cr', b'cardialogist'), (b'dr', b'dermatologist'), (b'en', b'endocrinologist'), (b'ent', b'ENT (Ear Nose Throat) Specialist'), (b'ge', b'Gerontologist'), (b'gy', b'Gynaecologist'), (b'ha', b'Haematologist'), (b'in', b'Internist'), (b'ne', b'Neurologist'), (b'ob', b'Obstetrician'), (b'on', b'Oncologist'), (b'op', b'Ophthalmologist'), (b'or', b'Orthodontist'), (b'ort', b'Orthopaedis'), (b'pd', b'Pediatrician'), (b'po', b'Podiatrist'), (b'ra', b'Radiologist'), (b'sr', b'Surgeon'), (b'ur', b'Urologist')])),
                ('graduation_university_name', models.CharField(max_length=200)),
                ('graduation_university_country', models.CharField(max_length=200)),
                ('graduation_university_city', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=2, choices=[(b'DE', b'dentist'), (b'GP', b'general practitioner'), (b'SP', b'Specialist'), (b'SSP', b'SSP')])),
                ('parent_hospital', models.ForeignKey(to='hospital.Hospital')),
            ],
            options={
            },
            bases=('hospital.staff',),
        ),
    ]
