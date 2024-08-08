from django.contrib import admin
from .models import Artisan, Client, Sector, SubscriptionFeature, SubscriptionPlan
# Register your models here.
@admin.register(Artisan, Client, Sector,SubscriptionFeature, SubscriptionPlan)
class UserAdmin(admin.ModelAdmin):
    pass