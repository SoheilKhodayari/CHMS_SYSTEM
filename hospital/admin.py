from django.contrib import admin

# Register your models here.
from hospital.models import Hospital,Phone

admin.site.register(Hospital)
admin.site.register(Phone)