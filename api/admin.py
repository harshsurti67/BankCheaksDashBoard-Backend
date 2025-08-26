from django.contrib import admin
from .models import UserData
# Register your models here.

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id','user_email','name', 'password')  # Customize the list display as needed