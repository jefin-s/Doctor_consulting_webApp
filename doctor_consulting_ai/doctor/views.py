from django.shortcuts import render
from doctor.models import Doctor
from login.models import Login
from django.http import HttpResponseRedirect
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

        ob=Login()
        ob.username=d.doctor_name
        ob.password=d.email
        ob.u_id=d.doctor_id
        ob.type='doctor'
        ob.save()
    return  render(request,'doctor/doctor.html')


def manage_doctor(request):
    d= Doctor.objects.all()
    mng_doctor = {
        'mng_dr': d
    }

    return  render(request,'doctor/manage_doctor.html',mng_doctor)


def accept_doctor(request,idd):
    d=Doctor.objects.get(pmr_id=idd)
    d.status='Accepted'
    d.save()
    return manage_doctor(request)

def reject_doctor(request,idd):
    d=Doctor.objects.get(doctor_id=idd)
    d.status="Reject"
    d.save()
    return  manage_doctor(request)

#
# def show(request):
#     d=Doctor.objects.get()
#     show_dr={
#         'show_dr':d
#     }
#     return