from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-patient/', views.createPatient, name="create-patient"),
    path('update-patient/<str:pk>/', views.updatePatient, name="update-patient"),
    path('delete-patient/<str:pk>/', views.deletePatient, name="delete-patient"),
    
    path('doctor_list/', views.docHome, name="doctor-list"),
    path('create-doctor/', views.createDoctor, name="create-doctor"),
    path('update-doctor/<str:pk>/', views.updateDoctor, name="update-doctor"),
    
    path('drone-list/', views.droneHome, name="drone-list"),
    path('create-drone/', views.createDrone, name="create-drone"),
    path('update-drone/<str:pk>/', views.updateDrone, name="update-drone"),
]














