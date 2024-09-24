from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)  # Ensure this is correctly named
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def _str_(self):
        return f"{self.first_name} {self.last_name}"