from django.shortcuts import render
from job.models import Job,AppliedJob
import datetime
from company.models import Company
# Create your views here.
def post_job(request):
    if request.method=='POST':
        ss=request.session['u_id']
        obj=Job()
        obj.job_name=request.POST.get('jobName')
        obj.desc=request.POST.get('jobDescription')
        obj.post_date=datetime.datetime.today()
        obj.location=request.POST.get('jobLocation')
        obj.vacancy=request.POST.get('jobVacancy')
        obj.job_nature=request.POST.get('jobNature')
        obj.salary=request.POST.get('jobSalary')
        obj.appli_date=request.POST.get('applicationDate')
        obj.skills=request.POST.get('jobSkills')
        obj.education=request.POST.get('jobEducation')
        obj.experience=request.POST.get('jobExperience')
        obj.company_id=ss
        obj.save()
    return render(request,'job/post_job.html')

def job_details(request,idd):
    obj=Job.objects.get(job_id=idd)
    context={
        'i':obj
    }
    return render(request,'job/job_details.html',context)


def job_listing(request):
    obj=Job.objects.all()
    context={
        'x':obj
    }
    return render(request,'job/job_listing.html',context)

def apply_job(request,idd):
    obj=Job.objects.get(job_id=idd)
    context={
        'x':obj
    }
    if request.method=='POST':
        ob=AppliedJob()
        ob.user_name=request.POST.get('fullName')
        ob.email=request.POST.get('email')
        ob.phone=request.POST.get('Phone')
        ob.resume=request.POST.get('resume')
        ob.appied_date=datetime.datetime.today()
        ob.job_id=obj.job_id
        ob.save()
    return render(request,'job/apply_job.html',context)

def view_application(request,idd):
    obj=AppliedJob.objects.filter(company_id=idd)
    context={
        'x':obj
    }
    return render(request,'job/view_applications.html',context)