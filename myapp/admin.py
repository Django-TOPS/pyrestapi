from django.contrib import admin
from .models import UserInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['name','branch','city']

admin.site.register(UserInfo,UserAdmin)
