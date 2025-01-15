from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('complaint_form/',views.complaint_form),
    url('manage/',views.manage_complaint),
    url('reply_complaint/(?P<idd>\w+)',views.reply_post_to_complaint),
    url('view_complaint/',views.view_complaint)

]