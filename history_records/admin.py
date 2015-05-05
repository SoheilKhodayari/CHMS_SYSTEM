from django.contrib import admin

from models import *

admin.site.register(MedicalFile)
admin.site.register(MedicationList)
admin.site.register(Disease)
admin.site.register(Surgery)
admin.site.register(X_ray)
admin.site.register(X_ray_area)
admin.site.register(X_ray_view)
admin.site.register(Ct)
admin.site.register(Ct_area)
admin.site.register(Test)
admin.site.register(Test_type)
admin.site.register(Mri)
admin.site.register(Mri_area)
admin.site.register(Medical_history_sheet)
admin.site.register(Physician_order_sheet)
admin.site.register(Progress_notes_sheet)
admin.site.register(Unit_summary_sheet)
admin.site.register(Order)
admin.site.register(Progress_note)