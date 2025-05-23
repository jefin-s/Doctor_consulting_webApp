from django.conf.urls import url
from patient import views

urlpatterns=[
    url('ptn_lgn/',views.login_patient),
    url('mng_ptnt/',views.manage_patient),
    url('apt/(?P<idd>\w+)', views.accept),
    url('rjct/(?P<idd>\w+)',views.reject),
    url('update_your_profile/',views.update_profile),
    url('patient_reg_app/',views.patient_reg_app.as_view()),
    url('sss/',views.viewww.as_view()),
    url('update/',views.update.as_view()),
    url('symptom/',views.sypmtoms.as_view())

]