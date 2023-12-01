from django.conf.urls import url
from job import views

urlpatterns=[
    url('post_job',views.post_job),
    url('job_details/(?P<idd>\w+)',views.job_details),
    url('job_listing',views.job_listing),
    url('apply_job/(?P<idd>\w+)',views.apply_job),
    url('view_applications/(?P<idd>\w+)',views.view_application),

]