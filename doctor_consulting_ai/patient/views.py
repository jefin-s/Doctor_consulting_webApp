from django.shortcuts import render
from patient.models import Patient
# Create your views here.
def login_patient(request):
    if request.method == "POST":
        p1=Patient()
        p1.patient_name = request.POST.get('patient_name')
        p1.username = request.POST.get('User_name')
        p1.password = request.POST.get('password')
        p1.gender = request.POST.get('gender')
        p1.email = request.POST.get('patient_email')
        p1.phone = request.POST.get('patient_phone')
        p1.status = 'pending'
        p1.save()



    return  render(request,'patient/patient.html')

def manage_patient(request):
    p1= Patient.objects.all()
    m_pt = {
        'mp': p1
    }
    return  render(request,'patient/manage_patient.html',m_pt)