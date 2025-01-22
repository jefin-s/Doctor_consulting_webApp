from django.shortcuts import render
from notifications.models import Notification
import  datetime
from doctor.models import Doctor
# Create your views here.
def post_notrification(request):
    nf=request.session['u_id']
    if request.method == 'POST':
        n1 = Notification()
        n1.notification_name = request.POST.get('ntf')
        n1.doctor_id=nf
        n1.date=datetime.datetime.today()
        n1.time=datetime.datetime.now()
        n1.save()


    return  render(request,'notifications/notifications.html')

def view_notifications(request):
    n1= Notification.objects.all()
    not_view = {
        'ntv': n1
    }
    return  render(request,'notifications/view_notification.html',not_view)
