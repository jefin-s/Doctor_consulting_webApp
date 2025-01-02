from django.shortcuts import render
from complaint.models import Complaint
import  datetime
# Create your views here.
def complaint_form(request):
    if request.method == 'POST':
        c = Complaint()
        c.complaints = request.POST.get('cmp')
        c.complaint_reply = 'pending'
        c.patient_id=1
        c.doctor_id=1
        c.date=datetime.datetime.today()
        c.time=datetime.datetime.now()
        c.save()



    return  render(request,'complaint/complaint.html')

def manage_complaint(request):
    c = Complaint.objects.all()
    manage_complaint={
        'manage':c
    }
    return render(request,'complaint/manage_complaint.html',manage_complaint)

def  reply_post_to_complaint(request):
    # c = Complaint.objects.all()
    # reply_complaint = {
    #     'reply': c
    # }
    return render(request,'complaint/post_reply.html',)

def view_complaint(request):
    c = Complaint.objects.all()
    vieww_complaint = {
        'view': c
    }
    return render(request,'complaint/view_complaint.html',vieww_complaint)
