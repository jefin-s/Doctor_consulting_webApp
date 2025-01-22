from django.shortcuts import render
from pmr.models import PatientMedicalReport
from patient.models import Patient
# Create your views here.
def craete_pmr(request):
    ob=Patient.objects.all()
    context={
        'x':ob
    }
    cpmr=request.session["u_id"]
    if request.method == 'POST':
        pmr=PatientMedicalReport()
        pmr.doctor_id=cpmr
        pmr.pateint_id=request.POST.get('pr')
        pmr.pmr_details=request.POST.get('pmr_doc')
        pmr.save()
    return  render(request,'pmr/Patient_medical_report.html', context)

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

