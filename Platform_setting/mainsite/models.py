from calendar import monthcalendar
from pyexpat import model
from django.db import models
from django.utils import timezone
from sklearn import inspection

# Create your models here.
#公佈欄資料庫表單
class news(models.Model):
    title = models.CharField(max_length=200,null=False)
    slug = models.CharField(max_length=200)
    body = models.TextField(null=False)
    pub_date = models.DateTimeField()
    nickname = models.CharField(max_length=20)
    press = models.IntegerField()
    catego = models.CharField(max_length=10)
    enabled = models.BooleanField()

    class Meta :
        ordering = ('-pub_date',)
    def __str__(self):
        return self.title

#設備總表
class Machine_System(models.Model):
    machine_system = models.CharField(max_length=10)

    def __str__(self):
        return self.machine_system

class Machine_Type(models.Model):
    SY = models.ForeignKey(Machine_System, on_delete=models.CASCADE)
    manchine_types = models.CharField(max_length=10)
    def __str__(self):
        return self.manchine_types

class Machine_Other_Setting(models.Model):
    MOS = models.ForeignKey(Machine_Type, on_delete=models.CASCADE)
    machine_number = models.CharField(max_length=50)
    machine_cabinet = models.CharField(max_length=10)
    machine_direction = models.CharField(max_length=5)
    machine_mile = models.CharField(max_length=10)
    def __str__(self):
        return self.machine_number

#隧道巡檢組別表資料庫
class Inspection(models.Model):
    inspection_date = models.DateTimeField(monthcalendar)
    inspection_group = models.CharField(max_length=10)


