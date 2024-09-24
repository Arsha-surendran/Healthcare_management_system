# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('patient','Patient'),
#         ('doctor','Doctor'),
#         ('admin','Admin'),
#     )
#     role = models.CharField(max_length=10,choices=ROLE_CHOICES)

# class PatientRecord(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     medical_history=models.TextField()
#     allergies=models.TextField()

# class Appointment(models.Model):
#     Patient=models.ForeignKey(User,related_name='appointments',on_delete=CASCADE)
#     doctor=models.ForeignKey(User,related_name='prescribed',on_delete=CASCADE)
#     date_time=models.DateTimeField()
#     notes=models.TextField()

# class Prescription(models.Model):
#     Patient=models.ForeignKey(User,related_name='prescriptions',on_delete=CASCADE)
#     doctor=models.ForeignKey(User,related_name='prescribed',on_delete=CASCADE)
#     medication=models.CharField(max_length=255)
#     dosage=models.CharField(max_length=255)
#     issued_date=models.DateField()
