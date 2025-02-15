from django.contrib import admin
from .models import * 
# Register your models here.

class SizeAdmin(admin.ModelAdmin):
    fields = ["size"]

class CheeseAdmin(admin.ModelAdmin):
    fields = ["cheese"]

class SauceAdmin(admin.ModelAdmin):
    fields = ["sauce"]



