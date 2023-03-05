from django.shortcuts import render, HttpResponse, redirect
from .models import Url
import uuid

def home(request):
  return render(request, 'myapp/home.html')

def create_url(request):
  if request.method == 'POST':
    link = request.POST.get('link')
    uid = str(uuid.uuid4())[:6]
    new_url = Url(link=link, uid=uid)
    new_url.save()
    return HttpResponse(f'http:127.0.1:8000/{uid}')


def create_custom(request):
  return render(request, 'myapp/custom_create.html')

def custom_create_url(request):
  if request.method == "POST":
    link = request.POST.get('link')
    uid = request.POST.get('custom_uid')
    try:
      already_exist = Url.objects.filter(uid=uid)
      if already_exist.exists():
        return HttpResponse('Already assigned to some other URL, Try some other word')
    except:
      pass
    new_url = Url(link=link, uid=uid).save()
    return HttpResponse(f'http:127.0.1:8000/{uid}')


def redirect_url(request, pk):
  url_details = Url.objects.get(uid=pk)
  return redirect(url_details.link)
