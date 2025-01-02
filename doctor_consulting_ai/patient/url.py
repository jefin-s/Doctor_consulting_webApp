from django.conf.urls import url
from patient import views

urlpatterns=[
    url('ptn_lgn/',views.login_patient),
    url('mng_ptnt',views.manage_patient),
]