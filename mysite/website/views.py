from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html', {})

def result(request):
    model=joblib.load('final_model.sav')
    per_depress=0
    return render(request,'result.html',{'per_depress':per_depress})
