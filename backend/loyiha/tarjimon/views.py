from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat
# Create your views here.
def salom(request):
   return HttpResponse("Salom dunyo")
def hello(request):
   return render(request ,'hello.html', {'ism':'Ramazon'})
def index(request):
   soz=request.GET.get('word',"")
   if soz and soz!='':
      natija=Lugat.objects.filter(inglizcha__contains=soz).all()[:3]
   else:
      natija=None
   return render(request,'index.html',{'word':soz,'natija':natija})

