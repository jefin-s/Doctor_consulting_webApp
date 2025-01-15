from django.conf.urls import url
from pmr import views

urlpatterns=[
    url('crt_pmr/',views.craete_pmr),
    url('updt_pmr/(?P<idd>\w+)',views.update_pmr),
    url('view_pmr_ptn',views.view_pmr_patient),

]