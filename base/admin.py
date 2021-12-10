from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name", "gender")
    search_fields = ("l_name__icontains", "f_name__icontains")
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name", "doc_phoneNumber")
    search_fields = ("l_name__icontains", "f_name__icontains")
    
@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ("drone_type", "drone_id", "user_id")
    search_fields = ("drone_type__icontains", "drone_id__icontains", "user_id__icontains")

admin.site.register(DroneUser)
admin.site.register(Admin)
admin.site.register(OutPatientDepartment_opd)



