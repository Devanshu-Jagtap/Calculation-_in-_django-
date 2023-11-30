from django.shortcuts import render,HttpResponse
from . models import *
# Create your views here.


def calculation(request):
    return render(request, 'index.html')
def addition(request):
     try:
        request.method == 'POST'
        Value1 = request.POST['Value1']
        Value2 = request.POST['Value2']
        result = int(Value1) + int(Value2)
        additions.objects.create(Value1=Value1, Value2=Value2,result=result)
        return render(request, 'addition.html', {'result': result})
     except:
         return render(request, 'addition.html', {'result': 0})

def subtraction(request):
     try:
        request.method == 'POST'
        Value1 = request.POST['Value1']
        Value2 = request.POST['Value2']
        result = int(Value1) - int(Value2)
        subtractions.objects.create(Value1=Value1, Value2=Value2,result=result)
        return render(request, 'subtraction.html', {'result': result})
     except:
         return render(request, 'subtraction.html', {'result': 0})

def multiplication(request):
     try:
        request.method == 'POST'
        Value1 = request.POST['Value1']
        Value2 = request.POST['Value2']
        result = int(Value1) * int(Value2)
        multiplications.objects.create(Value1=Value1, Value2=Value2,result=result)
        return render(request, 'multiplication.html', {'result': result})
     except:
         return render(request, 'multiplication.html', {'result': 0})

def division(request):
     try:
        request.method == 'POST'
        Value1 = request.POST['Value1']
        Value2 = request.POST['Value2']
        result = int(Value1) / int(Value2)
        divisions.objects.create(Value1=Value1, Value2=Value2,result=result)
        return render(request, 'division.html', {'result': result})
     except:
         return render(request, 'division.html', {'result': 0})

def addition_readData(request):
    add_data=addition.objects.all()
    print(add_data)
    return render(request,"Addition.html",{'addData': add_data})