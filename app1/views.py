from django.shortcuts import render

# Create your views here.
def generic(request):
    return render(request,'generic.html')

def generic1(request):
    return render(request,'generic1.html')