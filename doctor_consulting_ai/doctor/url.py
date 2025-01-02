from django.conf.urls import url
from doctor import views

urlpatterns=[
    url('doctor_reg/',views.doctor_registeration),
    url('manage_doctor/',views.manage_doctor),
]