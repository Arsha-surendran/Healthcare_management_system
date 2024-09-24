from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)  # Ensure this is correctly named
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def _str_(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"