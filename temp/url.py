from django.conf.urls import url
from temp import views

urlpatterns=[
    url('user_index',views.user_index),
    url('manager_index',views.manager_index),
    url('company_index',views.company_index),

]