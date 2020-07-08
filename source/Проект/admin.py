from django.contrib import admin

# Register your models here.
from .models import Проект
admin.site.register(Проект)

admin.site.site_title="НоТА"
admin.site.site_header="НоТА"
