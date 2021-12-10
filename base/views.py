from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q  

from .models import *
from .forms import *
# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    patients = Patient.objects.all().filter(
        Q(f_name__icontains=q) |
        Q(m_name__icontains=q) |
        Q(l_name__icontains=q) 
    )
    context = {'patients': patients}
    return render(request, 'base/home.html', context)

def createPatient(request):
    patients = Patient.objects.all()
    
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'patients': patients,
    }
    return render(request, 'base/create_patient.html', context)


def updatePatient(request, pk):
    patients = Patient.objects.get(id=pk)
    form = CreatePatientForm(instance=patients)
    if request.method == 'POST':
        form = CreatePatientForm(request.POST,instance=patients)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'patients': patients,
        'form': form,
    }
    
    return render(request, 'base/create_patient.html', context)


def deletePatient(request, pk):
    patients = Patient.objects.get(id=pk)
    
    if request.method == 'POST':
        patients.delete()
        return redirect('home')
    context = {'patients': patients}
    
    return render(request, 'base/delete_patient.html', context)
  
def docHome(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    doctors = Doctor.objects.all().filter(
        Q(f_name__icontains=q) |
        Q(m_name__icontains=q)|
        Q(l_name__icontains=q)
    )
    context = {'doctors': doctors}
    return render(request, 'base/doctor_list.html', context)
  
def createDoctor(request):
    doctors = Doctor.objects.all()
    form = createDoctorForm()
    
    if request.method == 'POST':
        form = createDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    context = {
        'doctors': doctors,
        'form': form,
    }
    return render(request, 'base/create_doctor.html', context)


def updateDoctor(request, pk):
    doctors = Doctor.objects.get(id=pk)
    form = createDoctorForm(instance=doctors)
    
    if request.method == 'POST':
        form = createDoctorForm(request.POST, instance=doctors)
        if form.is_valid():
            form.save()
            return redirect('doctor-list')
    context = {
        'doctors': doctors,
        'form': form,
    }
    return render(request, 'base/create_doctor.html', context)

def droneHome(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    drones = Drone.objects.all().filter(
        Q(drone_type__icontains=q)
    )
    context = {
        'drones': drones
    }
    return render(request, 'base/drone_list.html', context)

def createDrone(request):
    drones = Drone.objects.all()
    form = createDroneForm()
    
    if request.method == 'POST':
        form = createDroneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drone-list')
    
    context = {
            'drones': drones,
            'form': form,
        }
    return render(request, 'base/create_drone.html', context)

def updateDrone(request, pk):
    drones = Drone.object.get(id=pk)
    form = createDroneForm(instance=drones)
    
    if request.method == 'POST':
        form = createDroneForm(request.POST, instance=drones)
        if form.is_valid():
            form.save()
            return redirect('drone-list')
    
    context = {
        'drones': drones,
        'form': form
    }
    return render(request, 'base/create_drone.html', context)
                