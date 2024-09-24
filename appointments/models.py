from django.db import models

# Create your models here.
from patients.models import Patient
from doctors.models import Doctor


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def _str_(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"