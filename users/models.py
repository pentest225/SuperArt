from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACCOUNT_STATUS = [
    ('active', 'Actif'),
    ('unactive', 'Deactivé'),
    ('suspend', 'Suspendu'),
    ('wating', 'En Attante'),
]
SEX = [
    ('h', 'Homme'),
    ('f', 'Femme'),
]


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/')
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS, default='active')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class Sector(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class SubscriptionFeature(models.Model):
    name = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


PRICE_CHOICES = [
    ('/mois', 'Par mois'),
    ('/ans', 'Par Année'),
    ('/h', 'Par Heures'),
]


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    is_recommended = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=50, choices=PRICE_CHOICES)
    features = models.ManyToManyField(SubscriptionFeature)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS, default='active')
    sectors = models.ManyToManyField(Sector)
    bio = models.TextField(null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX, default='h')
    city = models.CharField(max_length=255, null=True, blank=True)
    location_lat = models.CharField(max_length=255, null=True, blank=True)
    location_lon = models.CharField(max_length=255, null=True, blank=True)
    study_level = models.CharField(max_length=255, null=True, blank=True)
    has_study_certify = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    WhatsApp_phone = models.CharField(max_length=10, null=True, blank=True)
    service_average = models.IntegerField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


MEDIA_TYPE = [
    ("fb", "Facebook"),
    ("tk", "TikTok"),
    ("yt", "Youtube"),
    ("int", "instagram"),
    ("wb", "website")
]


class ArtisanMediaLink(models.Model):
    artist = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50, choices=MEDIA_TYPE)
    url = models.URLField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
