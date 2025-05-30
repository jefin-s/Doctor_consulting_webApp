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

from rest_framework.views import APIView,Response
from django.http import HttpResponse
from login.serializers import android_serialiser

class loggg(APIView):
    def get(self,request):
        obj = Login.objects.all()
        ser = android_serialiser(obj, many=True)
        return Response(ser.data)

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        obj = Login.objects.filter(username=username, password=password)
        ser = android_serialiser(obj, many=True)
        return Response(ser.data)