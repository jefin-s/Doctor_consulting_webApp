from django.shortcuts import render
from doctor.models import Doctor
# Create your views here.
def doctor_registeration(request):
    if request.method == 'POST':
        d = Doctor()
        d.doctor_name = request.POST.get('doctor_name')
        d.departement = request.POST.get('doctor_category')
        d.experience = request.POST.get('doctor_experience')
        d.phone = request.POST.get('doctor_phone')
        d.qualification = request.POST.get('doctor_qualification')
        d.address = request.POST.get('doctor_address')
        d.date_of_birth=request.POST.get('date_of_birth')
        d.gender=request.POST.get('gender')
        d.email=request.POST.get('doctor_email')
        d.save()



    return  render(request,'doctor/doctor.html')


def manage_doctor(request):
    d= Doctor.objects.all()
    mng_doctor = {
        'mng_dr': d
    }

    return  render(request,'doctor/manage_doctor.html',mng_doctor)