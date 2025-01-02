from django.shortcuts import render
from pmr.models import PatientMedicalReport
# Create your views here.
def craete_pmr(request):
    if request.method == 'POST':
        pmr=PatientMedicalReport()
        pmr.doctor_id=1
        pmr.pateint_id=1
        pmr.pmr_details=request.POST.get('pmr_doc')
        pmr.save()
    return  render(request,'pmr/Patient_medical_report.html')

def update_pmr(request):
    # pmr=PatientMedicalReport.objects.all()
    # pmr_list={
    #     'pm':pmr
    # }
    return render(request,'pmr/update_pmr.html',pmr_list)

def view_pmr_patient(request):

    pmr=PatientMedicalReport.objects.all()
    pmr_v={
        'pmv':pmr
    }
    return  render(request,'pmr/view_pmr.html',pmr_v)