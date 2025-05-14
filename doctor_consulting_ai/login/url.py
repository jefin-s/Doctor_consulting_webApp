from django.conf.urls import url
from login import views

urlpatterns=[
    url('login/',views.login),
    url('logg/',views.loggg.as_view())
]