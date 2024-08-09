from django.contrib import admin

# Register your models here.
from services.models import Service, Tag, Message


@admin.register(Service, Tag, Message)
class ServiceAdmin(admin.ModelAdmin):
    pass
