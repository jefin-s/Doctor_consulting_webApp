from django.shortcuts import render
from booking_details.models import BookingDetails
from doctor.models import Doctor
import datetime
# Create your views here.
def booking_details(request):
    s1=request.session['u_id']
    ob=Doctor.objects.all()
    context={
        'bs':ob

    }
    if request.method == 'POST':
        b1 = BookingDetails()
        b1.booking_date = request.POST.get('date')
        b1.doctor_id = request.POST.get('doctor ')
        b1.patient_id = s1
        b1.booking_time = request.POST.get('time')
        
        b1.save()



    return  render(request, 'booking_details/Booking_details.html',context)


def booking_management(request):
    b1=BookingDetails.objects.all()
    booking_book={
        'book':b1
    }
    return  render(request,'booking_details/Booking_management.html',booking_book)

def booking_status_admin(request):
    b1 = BookingDetails.objects.all()
    booking_stat_admin_list = {
        'st_list': b1
    }

    return  render(request,'booking_details/booking_status_admin.html',booking_stat_admin_list)

def view_booking_details_patient(request):
    b1 = BookingDetails.objects.all()
    booking_det_pat = {
        'det_pat': b1
    }
    return render(request,'booking_details/view_booking_details_patient.html',booking_det_pat)


def booking_accept(request,idd):
    b1=BookingDetails.objects.get(booking_id=idd)
    b1.status="accepted"
    b1.save()
    return booking_management(request)


def booking_reject(request,idd):
    b1=BookingDetails.objects.get(booking_id=idd)
    b1.status="reject"
    b1.save()
    return booking_management(request)