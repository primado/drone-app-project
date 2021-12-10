from django.db import models

# Create your models here.
class Patient(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    
    patient_id = models.CharField(max_length=30, blank=True, null=True)
    admisiion_number = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=5, blank=True, null=True)
    f_name = models.CharField('First Name', max_length=20)
    m_name = models.CharField('Middle Name', max_length=20, blank=True, null=True)
    l_name = models.CharField('Last Name', max_length=20)
    marital_status = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=3, choices=GENDER, blank=True, null=True)
    dob = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=13, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    ghana_post_number = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    insurance_company = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        # name = self.f_name + " " + self.m_name + " " + self.l_name
        self.con = f"{self.f_name}, {self.m_name}, {self.l_name}"
        return self.con
    
class Doctor(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    
    doctor_id = models.CharField(max_length=15, blank=True, null=True)
    f_name = models.CharField('First Name', max_length=30)
    m_name = models.CharField('Middle Name', max_length=30, blank=True, null=True) 
    l_name = models.CharField('Last Name', max_length=30)
    doc_phoneNumber = models.CharField("Phone Number", max_length=20, blank=True, null=True)
    doc_email = models.CharField("Email", max_length=60, blank=True, null=True)
    patient = models.ForeignKey(Patient, null=True, on_delete= models.SET_NULL) 
    create_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=3, choices=GENDER, blank=True, null=True)
    
    
    
    def __Str__(self):
        return f"{self.f_name}, {self.m_name}, {self.l_name}"

class Drone(models.Model):
    drone_id = models.CharField('Drone ID', max_length=10, blank=True, null=True)
    drone_type = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField('User ID',max_length=10, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.drone_type

class DroneUser(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    
    user_id = models.CharField(max_length=20, blank=True, null=True)
    f_name = models.CharField('First Name', max_length=30, blank=True, null=True)
    l_name = models.CharField('Last Name', max_length=30, blank=True, null=True)
    drone_type = models.CharField(max_length=20, blank=True, null=True)
    #drone_id = models.CharField(max_length=10, blank=True, null=True)
    drone = models.ForeignKey(Drone, null=True, on_delete= models.SET_NULL)
    create_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=3, choices=GENDER, blank=True, null=True)
    

    def __str__(self):
        return self.f_name + " " + self.l_name

class Admin(models.Model):
    user_name = models.CharField('Username',max_length=60, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class OutPatientDepartment_opd(models.Model):
    opd_number = models.CharField(max_length=30,blank=True, null=True)
    # patient_id = CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    temperature = models.CharField(max_length=10, blank=True, null=True)
    patient_complains = models.TextField(max_length=200, blank=True, null=True)
    patient = models.ForeignKey(Patient, null=True, on_delete= models.SET_NULL)
    create_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.temperature