from django.conf.urls import url
from booking_details import  views

urlpatterns=[
    url('bkng_details/',views.booking_details),
    url('mng_bkng/',views.booking_management),
    url('bkng_status_admin/',views.booking_status_admin),
    url('bkng_details_pateint',views.view_booking_details_patient),
 ]