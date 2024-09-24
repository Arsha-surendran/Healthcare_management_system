from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

# View to add a new doctor
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to the doctor list view
    else:
        form = DoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})

# View to list all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

# View to update a doctor's information
def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to the doctor list view
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/update_doctor.html', {'form': form})

# View to delete a doctor
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')  # Redirect to the doctor list view
    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})