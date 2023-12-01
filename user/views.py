from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
def user_register(request):
    if request.method=='POST':
        obj=User()
        obj.f_name=request.POST.get('firstName')
        obj.m_name=request.POST.get('middleName')
        obj.l_name=request.POST.get('lastName')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.address=request.POST.get('address')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status="pending"
        obj.save()
    return render(request,'user/user_register.html')

def manage_user(request):
    obj=User.objects.all()
    context={
        'x':obj
    }
    return render(request,'user/manage_user.html',context)

def approve(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="approved"
    obj.save()
    ob=Login()
    ob.username=obj.username
    ob.password=obj.password
    ob.type="user"
    ob.u_id=obj.user_id
    ob.save()
    return manage_user(request)

def reject(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="reject"
    obj.save()
    return manage_user(request)
   