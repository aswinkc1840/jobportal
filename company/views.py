from django.shortcuts import render
from company.models import Company
from login.models import Login
from django.core.files.storage import FileSystemStorage


# Create your views here.
def  company_register(request):
    if request.method=='POST':
        obj=Company()
        obj.company_name=request.POST.get('companyName')
        # obj.logo=request.POST.get('companyImage')

        myfile=request.FILES['clogo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.logo=myfile.name 

        obj.desc=request.POST.get('companyDesc')
        obj.website=request.POST.get('companyWebsite')
        obj.email=request.POST.get('companyEmail')
        obj.phone=request.POST.get('companyPhone')
        obj.location=request.POST.get('companyLocation')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()
        
    return render(request,'company/company_register.html')


def manage_company(request):
    obj=Company.objects.all()
    context={
        'x':obj
    }
    return render(request,'company/manage_company.html',context)

def approve(request,idd):
    obj=Company.objects.get(company_id=idd)
    obj.status='Approved'
    obj.save()
    ob=Login()
    ob.username=obj.username
    ob.password=obj.password
    ob.type="company"
    ob.u_id=obj.company_id
    ob.save()
    return manage_company(request)

def reject(request,idd):
    obj=Company.objects.get(company_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage_company(request)