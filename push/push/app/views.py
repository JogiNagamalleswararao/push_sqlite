from django.shortcuts import render,HttpResponse
from .models import Push

def home(requset):
    if requset.method == 'POST':
        name = requset.POST['name']
        email = requset.POST['email']
        obj=Push()
        obj.name=name
        obj.email=email
        obj.save()
    return render(requset,"index.html")
# Create your views here.
