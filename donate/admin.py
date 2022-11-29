from django.contrib import admin
from .models import Ecpay,Opay,Streamer
# Register your models here.
@admin.register(Opay)
class OpayAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Opay._meta.get_fields()][1:]
    pass