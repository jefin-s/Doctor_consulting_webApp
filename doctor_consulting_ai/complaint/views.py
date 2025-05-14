from django.shortcuts import render
from complaint.models import Complaint
import  datetime
from doctor.models import Doctor
from rest_framework.views import APIView,Response
from django.http import  HttpResponse
from complaint.serializers import android_serilaizers
# Create your views here.
def complaint_form(request):
    cs=request.session['u_id']
    ob=Doctor.objects.all()
    context={
            'c':ob
        }

    if request.method == 'POST':
        c = Complaint()
        c.complaints = request.POST.get('cmp')
        c.complaint_reply = 'pending'
        c.patient_id=cs
        c.doctor_id=request.POST.get('complaint')
        c.date=datetime.datetime.today()
        c.time=datetime.datetime.now()
        c.save()
    return  render(request,'complaint/complaint.html',context)

def manage_complaint(request):
    c = Complaint.objects.all()
    manage_complaint={
        'manage':c
    }
    return render(request,'complaint/manage_complaint.html',manage_complaint)

def  reply_post_to_complaint(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.complaint_reply=request.POST.get('rply')
        obj.save()
        return manage_complaint(request)
    return render(request,'complaint/post_reply.html',)

def view_complaint(request):
    c = Complaint.objects.all()
    vieww_complaint = {
        'view': c
    }
    return render(request,'complaint/view_complaint.html',vieww_complaint)

class compaint_app(APIView):
    def post(self,request):
        obj=Complaint()
        obj.complaints=request.data['complaints']
        obj.complaint_reply='pending'
        obj.doctor_id=request.data['did']
        obj.patient_id=request.data['pid']
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
        return HttpResponse('complaint')

