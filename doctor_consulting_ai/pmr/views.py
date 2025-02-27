from django.shortcuts import render
from pmr.models import PatientMedicalReport
from patient.models import Patient
from rest_framework.views import APIView,Response
from pmr.serailizers import android_serializers

# Create your views here.
def craete_pmr(request):
    ss=request.session["u_id"]
    ob=Patient.objects.all()
    context={
        'x':ob
    }
    if request.method == 'POST':
        pmr=PatientMedicalReport()
        pmr.doctor_id=ss
        pmr.name=request.POST.get('pr')
        pmr.age=request.POST.get('age')
        pmr.phone=request.POST.get('phone')
        pmr.address=request.POST.get('address')
        pmr.category=request.POST.get('category')
        pmr.gender=request.POST.get('gender')
        pmr.date=request.POST.get('date')
        pmr.time=request.POST.get('time')
        pmr.prescription=request.POST.get('prescriptions')
        pmr.save()
    return render(request,'pmr/Patient_medical_report.html',context)

def pmr_view_only(request):
    pmr=PatientMedicalReport.objects.all()
    pmr_o={
        'pmv':pmr
    }
    return render(request,'pmr/view_pmr_only.html',pmr_o)

def update_pmr(request,idd):
    pmr = PatientMedicalReport.objects.get(pmr_id=idd)
    pmr_v = {
        'pmv': pmr
    }
    if request.method == 'POST':
        pmr=PatientMedicalReport.objects.get(pmr_id=idd)
        pmr.pmr_details=request.POST.get('upd')
        pmr.save()
        return view_pmr_patient(request)
    return render(request,'pmr/update_pmr.html',pmr_v)

def view_pmr_patient(request):

    pmr=PatientMedicalReport.objects.all()
    pmr_v={
        'pmv':pmr
    }
    return  render(request,'pmr/view_pmr.html',pmr_v)


class view_pmr_app(APIView):
    def get(self,request):
        obj=PatientMedicalReport.objects.all()
        ser=android_serializers(obj,many=True)
        return Response(ser.data)

