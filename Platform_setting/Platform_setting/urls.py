"""Platform_setting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from mainsite.views import sayhi1, sayhi5,sayhi6,homepage, showpost,create_form,machine_month,base_machine_select_form,machine_form_one,event_record,inspection

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('newyear/(\w+)/$',sayhi5),
    re_path('now/(\w+)/$',sayhi6),
    path('',homepage),
    path('post/<slug:slug>/', showpost),
    path('create/',create_form),
    path('machine_month/',machine_month ),
    path('base_machine_select_form/', base_machine_select_form),
    path('base_machine_select_form/machine_form_one', machine_form_one),
    path('event_record/', event_record),
    path('inspection/', inspection),
]
