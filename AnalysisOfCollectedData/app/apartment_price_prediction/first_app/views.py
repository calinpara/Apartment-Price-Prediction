from django.shortcuts import render
from django.http import HttpResponse

import joblib

# Create your views here.

def home(request):


    return render(request, 'first_app/home.html')


def result(request):

    model = joblib.load('appartment_price_prediction_model.sav')

    lst = list()

    lst.append(request.GET['Nr. camere'])
    lst.append(request.GET['Suprafata construita'])
    lst.append(request.GET['Etaj'])
    lst.append(request.GET['Nr. bai'])
    lst.append(request.GET['An constructie'])
    lst.append(request.GET['Nr. balcoane'])
    lst.append(request.GET['Zona'])
    lst.append(request.GET['Finalizat/In constructie'])
    lst.append(request.GET['Inchise/Deschise'])
    print(lst)

    arr = model.predict([lst])
    print(arr)
    answer = int(arr[0])
    print(answer)

    return render(request, 'first_app/results.html',{'answer': answer} )