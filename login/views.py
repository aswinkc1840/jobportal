from django.http import HttpResponseRedirect
from django.shortcuts import render

from login.models import Login

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Login.objects.filter(username=username,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/manager_index')
            elif tp=="user":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/user_index')
            elif tp=="company":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/company_index')
        else:
            objlist="incorrect username or password......"
            context={
                    'x':objlist,
                }
            return render(request,'login/login2.html',context)

    return render(request,'login/login2.html')


def logout(request):
    return render(request,'login/login2.html')