from django.contrib import admin
from frontend.models import *
# Register your models here.
@admin.register(HomeCarouselImage)
class DocumentAdmin(admin.ModelAdmin):
    pass