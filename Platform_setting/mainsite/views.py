from threading import local
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import news
from datetime import datetime
# Create your views here.
# Create your views here.

def sayhi1 (request):
    return HttpResponse('你好歡迎光臨')

def sayhi5 (request, myname):
    return HttpResponse(myname+'您好新年快樂')


# 將所有views.py的變數都傳到模板templates（sayhi6.html)的方法：
# return render(request,'模板網頁',locals())
def sayhi6(request, myname):
    now = datetime.today()
    return render (request,'sayhi6.html',locals())

def homepage(request):
    posts = news.objects.all()
    now = datetime.now
    return render (request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = news.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


#設備管理部分
def create_form(request):
    return render(request, 'create.html', locals())
def machine_month(request):
    return render(request,'machine_month.html', locals())

def base_machine_select_form(request):
    return render(request,'base_machine_select_form.html', locals())
def machine_form_one(request):
    return render(request,'machine_form_one.html', locals())
def event_record(request):
    return render(request,'event_record.html', locals())
def inspection(request):
    return render(request,'event_record.html', locals())
