from django.contrib import admin
from myapp.models import MyUserData

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone','place',)
    search_fields = ('username',)

admin.site.register(MyUserData,UserAdmin)


