from django.contrib import admin
from .models import *

@admin.register(Bolim)
class BolimAdmin(admin.ModelAdmin):
    list_display = ['nom', 'haqida']

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ['ism', 'mamlakat']


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ['nom', 'muallif']
