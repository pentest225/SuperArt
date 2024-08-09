from django.db import models


# Create your models here.
class AppInfo(models.Model):
    home_title = models.TextField(max_length=100)
    app_name = models.TextField(max_length=100)
    app_description = models.TextField(max_length=100)
    phone = models.TextField(max_length=15)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    facebook = models.TextField(max_length=100)
    instagram = models.TextField(max_length=100)
    linkedin = models.TextField(max_length=100)
    tiktok = models.TextField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class HomeCarouselImage(models.Model):
    image = models.ImageField(upload_to='homeCarouselImages/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.image.name
