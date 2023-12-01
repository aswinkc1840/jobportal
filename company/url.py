from django.conf.urls import url
from company import views

urlpatterns=[
    url('company_register',views.company_register),
    url('manage_company',views.manage_company),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),

]