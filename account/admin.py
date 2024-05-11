from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at']

# Register your models here.
