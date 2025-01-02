from django.shortcuts import render
from ai_solutions.models import AiSolutions
# Create your views here.
def feedback(request):
    if request.method == 'POST':
        obj = AiSolutions()
        obj.solutions = request.POST.get('solution')
        obj.patient_id = 1
        obj.doctor_id =1
        obj.save()
    return render(request, 'ai_solutions/Feedback.html')


def viewsolution(request):
    obj = AiSolutions.objects.all()
    context = {
        'a':obj
    }
    return render(request, 'ai_solutions/view_solutions.html', context)