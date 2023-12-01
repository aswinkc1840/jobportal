from django.conf.urls import url
from user import views

urlpatterns=[
    url('user_register',views.user_register),
    url('manage_user',views.manage_user),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),


]