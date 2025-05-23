from django.shortcuts import render
from patient.models import Patient
from rest_framework.views import APIView,Response
from patient.serializers import android_seriliazers
from django.http import HttpResponse
from doctor_consulting_ai import settings
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# Create your views here.
def login_patient(request):
    if request.method == "POST":
        p1=Patient()
        p1.patient_name = request.POST.get('patient_name')
        p1.username = request.POST.get('User_name')
        p1.password = request.POST.get('password')
        p1.gender = request.POST.get('gender')
        p1.email = request.POST.get('patient_email')
        p1.phone = request.POST.get('patient_phone')
        p1.status = 'pending'
        p1.save()
    return  render(request,'patient/patient.html')

def manage_patient(request):
    p1= Patient.objects.all()
    m_pt = {
        'mp': p1
    }
    return  render(request,'patient/manage_patient.html',m_pt)


def accept(request,idd):
    obj=Patient.objects.get(patient_id=idd)
    obj.status='Accepted'
    obj.save()
    return manage_patient(request)

def reject(request,idd):
    p1=Patient.objects.get(patient_id=idd)
    p1.status="rejected"
    p1.save()
    return  manage_patient(request)

def update_profile(request,):
    p1 = Patient.objects.all()
    context = {
        's':p1
    }
    if request.method == "POST":
        p1 = Patient.objects.get(patient_id=idd)
        p1.patient_name = request.POST.get('patient_name')
        p1.username = request.POST.get('User_name')
        p1.password = request.POST.get('password')
        p1.gender = request.POST.get('gender')
        p1.email = request.POST.get('patient_email')
        p1.phone = request.POST.get('patient_phone')
        p1.status = 'pending'
        p1.save()
    return render(request,'patient/updte_ptn_profile.html', context)
from login.models import Login
class patient_reg_app(APIView):
    def post(self,request):
        obj=Patient()
        obj.patient_name = request.data['patient_name']
        obj.username = request.data['username']
        obj.password = request.data['password']
        obj.gender = request.data['gender']
        obj.email = request.data['email']
        obj.phone = request.data['phone']
        obj.status = 'pending'
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.u_id=obj.patient_id
        ob.type='patient'
        ob.save()
        return HttpResponse('patient_register')

class viewww(APIView):
    def post(self,request):
        ob=Patient.objects.filter(patient_id=request.data['k'])
        ser=android_seriliazers(ob,many=True)
        return Response(ser.data)

class update(APIView):
    def post(self,request):
        ob=Patient.objects.get(patient_id=request.data['k'])
        ob.patient_name = request.data['name']
        ob.username = request.data['username']
        ob.password = request.data['password']
        ob.gender = request.data['gender']
        ob.email = request.data['email']
        ob.phone = request.data['phone']
        ob.status = 'pending'
        ob.save()
        return HttpResponse("yes")





class sypmtoms(APIView):
    def post(self,request):
        itching=request.data['itching']
        print(itching)
        Skin_rash=request.data['Skin_rash']
        print(Skin_rash)
        nodal_skin_eruption=request.data['nodal_skin_eruption']
        print(nodal_skin_eruption)
        sneezing=request.data['sneezing']
        print(sneezing)
        Shivering=request.data['Shivering']
        print(Shivering)
        Chiils=request.data['Chiils']
        print(Chiils)
        Joint_pain=request.data['Joint_pain']
        print(Joint_pain)
        Stomach_pain=request.data['Stomach_pain']
        print(Stomach_pain)
        Acidity=request.data['Acidity']
        print(Acidity)
        Chronic_cough=request.data['Chronic_cough']
        print(Chronic_cough)
        Ulcer_on_mouth=request.data['Ulcer_on_mouth']
        print(Ulcer_on_mouth)
        Vomiting=request.data['Vomiting']
        print(Vomiting)
        Fever=request.data['Fever']
        print(Fever)
        Shorteness_breathe=request.data['Shorteness_breathe']
        print(Shorteness_breathe)
        fatigue=request.data['fatigue']
        print(fatigue)
        Weight_gain=request.data['Weight_gain']
        print(Weight_gain)
        Anxiety=request.data['Anxiety']
        print(Anxiety)
        Pain_radiating_arm=request.data['Pain_radiating_arm']
        print(Pain_radiating_arm)
        Mood_swings=request.data['Mood_swings']
        print(Mood_swings)
        Wheezing=request.data['Wheezing']
        print(Wheezing)
        Headaches=request.data['Headaches']
        print(Headaches)
        Burping=request.data['Burping']
        print(Burping)
        Memoryloss=request.data['Memoryloss']
        print(Memoryloss)
        dizziness=request.data['dizziness']
        print(dizziness)
        Chest_pain=request.data['Chest_pain']
        print(Chest_pain)

        test=[int(itching), int(Skin_rash), int(nodal_skin_eruption), int(sneezing), int(Shivering), int(Chiils), int(Joint_pain),int(Stomach_pain),int(Acidity),int(Chronic_cough),int(Ulcer_on_mouth),int(Vomiting),int(Fever),int(Shorteness_breathe),int(fatigue),int(Weight_gain),int(Anxiety),int(Pain_radiating_arm),int(Mood_swings),int(Wheezing),int(Headaches),int(Burping),int(Memoryloss),int(dizziness),int(Chest_pain)]


        dspath=str(settings.BASE_DIR)+str(settings.STATIC_URL)+"dataset.xlsx"

        df=pd.read_excel(dspath)

        # print(df.head(2))
        dtc=DecisionTreeClassifier()
        # input
        xatr=['itching','rash','nodal','sneezing','shivering','chills','joint','stomach','acidity','chronic','ulcer','vomiting','fever','breath','fatigue','weight','anxiety','arm','swings','wheezing','headches','burping','memory','dizziness','chest']
        #ouput

        print(xatr)
        yatr="prognosis"

        X=df.loc[:,xatr]
        y=df.loc[:,yatr]

        dtc.fit(X,y)

        res=dtc.predict([test])

        print((res[0]))



        return HttpResponse(res[0])

