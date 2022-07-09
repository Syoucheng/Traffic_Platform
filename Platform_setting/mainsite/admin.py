from django.contrib import admin
from regex import E
from .models import news,Machine_System,Machine_Type,Machine_Other_Setting
# Register your models here.
class newsAdmin(admin.ModelAdmin):
    list_display = ('nickname','title','body' ,'pub_date' ,'enabled','press' ,'catego')

admin.site.register(news,newsAdmin) 
admin.site.register(Machine_System)
admin.site.register(Machine_Other_Setting)
admin.site.register(Machine_Type)



