from django.conf.urls import url
from temp import views

urlpatterns=[
    url('admin/',views.admin),
    url('doctor/',views.doctor),
    url('patient/',views.patient),
    url('home/',views.home)
]