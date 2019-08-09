from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import IstUser
# Register your models here.
class IstUserAdmin(UserAdmin):
    model = IstUser
    list_display = ['pk', 'username']

admin.site.register(IstUser, IstUserAdmin)