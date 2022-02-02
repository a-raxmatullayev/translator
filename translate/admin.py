from django.contrib import admin
from .models import tarjima
# Register your models here.

class Dictionary(admin.ModelAdmin):

    list_display = ['inglizcha', 'uzbekcha']

admin.site.register(tarjima, Dictionary)
