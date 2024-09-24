from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_appointment, name='add_appointment'),  # URL for adding a new appointment
    path('alist/', views.appointment_list, name='appointment_list'),    # URL for listing all appointments
    path('update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),  # URL for updating an appointment
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),  # URL for deleting an appointment
]