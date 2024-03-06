from django.contrib import admin

from .models import MyClient

class MyClientAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in MyClient._meta.fields if field.name != "id"
    ]
    
admin.site.register(MyClient, MyClientAdmin)
