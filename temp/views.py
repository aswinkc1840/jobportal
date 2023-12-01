from django.shortcuts import render
from company.models import Company
from job.models import Job
# Create your views here.
def user_index(request):
    return render(request,'temp/user_index.html')

def manager_index(request):
    return render(request,'temp/manager_index.html')

def company_index(request):
    ss=request.session['u_id']
    context={
        'x':ss
    }
    return render(request,'temp/company_index.html',context)