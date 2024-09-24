from django.urls import path
from .import views

urlpatterns = [
    path('add/doctor/', views.add_doctor, name='add_doctor'),
    path('dlist/', views.doctor_list, name='doctor_list'),
    path('update/<int:doctor_id>/',views.update_doctor,name='update_doctor'),
    path('delete/<int:doctor_id>/',views.delete_doctor,name='delete_doctor'),
]