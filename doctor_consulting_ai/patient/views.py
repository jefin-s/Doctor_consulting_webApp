from django.shortcuts import render
from patient.models import Patient
from rest_framework.views import APIView,Response
from patient.serializers import android_seriliazers
from django.http import HttpResponse
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


def accept(request,idd):
    obj=Patient.objects.get(patient_id=idd)
    obj.status='Accepted'
    obj.save()
    return manage_patient(request)

def reject(request,idd):
    p1=Patient.objects.get(patient_id=idd)
    p1.status="rejected"
    p1.save()
    return  manage_patient(request)

def update_profile(request,):
    p1 = Patient.objects.all()
    context = {
        's':p1
    }
    if request.method == "POST":
        p1 = Patient.objects.get(patient_id=idd)
        p1.patient_name = request.POST.get('patient_name')
        p1.username = request.POST.get('User_name')
        p1.password = request.POST.get('password')
        p1.gender = request.POST.get('gender')
        p1.email = request.POST.get('patient_email')
        p1.phone = request.POST.get('patient_phone')
        p1.status = 'pending'
        p1.save()
    return render(request,'patient/updte_ptn_profile.html', context)

class patient_reg_app(APIView):
    def post(self,request):
        obj=Patient()
        obj.patient_name = request.data['patient_name']
        obj.username = request.data['username']
        obj.password = request.data['password']
        obj.gender = request.data['gender']
        obj.email = request.data['email']
        obj.phone = request.data['phone']
        obj.status = 'pending'
        obj.save()
        return HttpResponse('patient_register')



class updt_prfl_app(APIView):
    def post(self,request):
        obj = Patient()
        obj.patient_name = request.data['patient_name']
        obj.username = request.data['username']
        obj.password = request.data['password']
        obj.gender = request.data['gender']
        obj.email = request.data['email']
        obj.phone = request.data['phone']
        obj.status = 'pending'
        obj.save()
        return HttpResponse('update_profile')