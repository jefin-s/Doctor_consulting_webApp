from django.conf.urls import  url
from notifications import views

urlpatterns=[
    url('post_ntfn/',views.post_notrification),
    url('view_ntfn/',views.view_notifications),
    url('view_nfn',views.view_notfn_app.as_view())
]