from django.contrib import admin

from .models import *

@admin.register(User)
class ModelAdmin(admin.ModelAdmin):
    list_display=['email','mobile','is_verified','email_tokan','forget_password']
# admin.site.register(User)