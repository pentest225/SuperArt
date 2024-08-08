from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACCOUNT_STATUS = [
    ('active', 'Actif'),
    ('unactive', 'Deactivé'),
    ('suspend', 'Suspendu'),
    ('waiting', 'En Attante'),
]

SEX = [
    ('h', 'Homme'),
    ('f', 'Femme'),
]


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/',blank=True)
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

    def __str__(self):
        return self.name


class SubscriptionFeature(models.Model):
    name = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan,on_delete=models.CASCADE, related_name='subscription_plan_artisan',null=True,blank=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS, default='waiting')
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE, related_name='sector_artisan', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX, default='h')
    city = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location_lat = models.CharField(max_length=255, null=True, blank=True)
    location_lon = models.CharField(max_length=255, null=True, blank=True)
    study_level = models.CharField(max_length=255, null=True, blank=True)
    has_study_certify = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    whatsApp_phone = models.CharField(max_length=10, null=True, blank=True)
    service_average = models.IntegerField(default=0, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


MEDIA_TYPE = [
    ("fb", "Facebook"),
    ("tk", "TikTok"),
    ("yt", "Youtube"),
    ("int", "instagram"),
    ("wb", "website"),
    ("tw", "Twitter"),
]


class ArtisanMediaLink(models.Model):
    artist = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50, choices=MEDIA_TYPE)
    url = models.URLField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
