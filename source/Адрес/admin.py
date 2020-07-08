from django.contrib import admin

# Register your models here.

from .models import Адрес
# @admin.register(Адрес)
# class АдресAdmin(admin.ModelAdmin):

admin.site.register(Адрес)