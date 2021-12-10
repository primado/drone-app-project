from django.forms import ModelForm

from .models import *


class CreatePatientForm(ModelForm):
    
    class Meta:
        model = Patient
        fields = ['f_name', 'm_name', 'l_name', 'gender', 'nationality', 
                  'house_number', 'region', 'phone_number', 'email'
                ]

class createDoctorForm(ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['f_name', 'm_name', 'l_name', 'doc_phoneNumber', 'gender', 'doc_email', 'patient']

class createDroneForm(ModelForm):
    
    class Meta:
        model = Drone
        fields = ['drone_id', 'drone_type']