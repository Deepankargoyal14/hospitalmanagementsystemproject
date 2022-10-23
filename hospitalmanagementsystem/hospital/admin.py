from django.contrib import admin

from hospital.models import Patient,LoginTable

class PatientModel(admin.ModelAdmin):
    list_display = ('Patient_name','gender','phonenumber','birthdate','bloodgroup')
# Register your models here.
admin.site.register(Patient,PatientModel)
admin.site.register(LoginTable)
