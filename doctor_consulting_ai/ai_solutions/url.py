from django.conf.urls import url
from ai_solutions import views

urlpatterns = [
    url('fdbck/', views.feedback),
    url('viewslm/', views.viewsolution)
]