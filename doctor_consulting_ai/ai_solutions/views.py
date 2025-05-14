from django.shortcuts import render
from ai_solutions.models import AiSolutions
from patient.models import Patient
from rest_framework.views import APIView,Response
from ai_solutions.serilaisers import android_serializers
from django.http import HttpResponse

# Create your views here.
def feedback(request):
    ss=request.session['u_id']
    ob=Patient.objects.all()
    context={
        'sbox':ob
    }
    if request.method == 'POST':
        obj = AiSolutions()
        obj.solutions = request.POST.get('solution')
        obj.patient_id = request.POST.get('patient')
        obj.doctor_id =ss
        obj.save()
    return render(request, 'ai_solutions/Feedback.html',context)


def viewsolution(request):
    obj = AiSolutions.objects.all()
    context = {
        'a':obj
    }
    return render(request, 'ai_solutions/view_solutions.html', context)

class solution_view(APIView):
    def get(self,request):
        obj=AiSolutions.objects.all()
        ser=android_serializers(obj,many=True)
        return Response(ser.data)
