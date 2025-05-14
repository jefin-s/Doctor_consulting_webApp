from django.conf.urls import url

# from ai_solutions import url

from doctor import views

urlpatterns=[
    url('doctor_reg/',views.doctor_registeration),
    url('manage_doctor/',views.manage_doctor),
    url('acpt_dr/(?P<idd>\w+)',views.accept_doctor),
    url('rjct_dr/(?P<idd>\w+)',views.reject_doctor),
    url('view_doc/', views.view_doc.as_view())

]