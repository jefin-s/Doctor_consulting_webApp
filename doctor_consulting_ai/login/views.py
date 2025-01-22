from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method =='POST':
        uname=request.POST.get("uname")
        passw=request.POST.get("psw")
        obj = Login.objects.filter(username=uname,password=passw)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session['u_id'] =uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "doctor":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/doctor/')

            else:
                objlist="Username name or Password incorrect ... please try again"
                context={
                    'msg':objlist
                }
                return render(request,'login/login.html',context)


    return render (request,'login/login.html')