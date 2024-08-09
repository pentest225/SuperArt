from django.db import models
from users.models import Artisan, Sector, PRICE_CHOICES, Client, User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


SERVICE_STATUS = [
    ('active', 'Active'),
    ('suspend', 'Suspend'),
    ('disabled', 'Disabled'),
    ('waiting', 'Waiting'),
]


class Service(models.Model):
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, related_name='artisan_services')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_service')
    main_image = models.ImageField(upload_to='services')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=50, choices=PRICE_CHOICES)
    city = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location_lat = models.CharField(max_length=255, null=True, blank=True)
    location_lon = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=50, choices=SERVICE_STATUS, default='active')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ',' + self.artisan.sector.name

    def get_rating_average(self):
        rating = [rating.rating for rating in self.service_rating.all()]
        if len(rating) == 0:
            return 0
        return sum(rating) / len(rating)


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_images')
    image = models.ImageField(upload_to='services')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


ORDER_STATUS = [
    ('pending', 'En attente'),
    ('confirmed', 'Confirmée'),
    ('cancelled', 'Rejetée'),
]


class ServiceOrder(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_order')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_service_order')
    reservation_date = models.DateField()
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='pending')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


MESSAGE_CHANEL = [
    ('message', 'Message'),
    ('whatsapp', 'WhatsApp'),
    ('email', 'Email'),
    ('sms', 'SMS'),
]


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_message')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_message')
    chanel = models.CharField(max_length=50, null=True, blank=True, choices=MESSAGE_CHANEL, default='message')
    content = models.TextField()
    is_read = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class ServiceRating(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_rating')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_rating', null=True, blank=True)
    rating = models.IntegerField(default=0)
    service_rating = models.IntegerField(default=0)
    value_for_money = models.IntegerField(default=0)

    message = models.TextField()
    rating_like = models.PositiveIntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class RatingImage(models.Model):
    rating = models.ForeignKey(ServiceRating, on_delete=models.CASCADE, related_name='service_rating_images')
    image = models.ImageField(upload_to='ratings')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class ClientRequirement(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_requirement')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_requirement')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location_address = models.CharField(max_length=100)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='pending')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
