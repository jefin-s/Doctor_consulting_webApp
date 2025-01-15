from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')


def doctor(request):
    return render(request,'temp/Doctor.html')


def patient(request):
    return render(request,'temp/patient.html')

def home(request):
    return render(request,'temp/home.html')