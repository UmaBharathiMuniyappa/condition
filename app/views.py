from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':11,'b':12,'c':15}
    return render(request,'condition.html',d)