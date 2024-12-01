from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now
from home.models import Certificate
import pycountry



class Profile(models.Model):
    AVAILABLE_COUNTRIES = [(country.alpha_2, country.name) for country in pycountry.countries]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='app_pictures/default_profile_pic.jpg', upload_to='profile_pictures/')
    first_name = models.CharField(max_length=30, default="Unnamed")
    last_name = models.CharField(max_length=30, default="Diver")
    about_profile = models.TextField(default="")
    birth_date = models.DateField(blank=True, null=True)
    registration_date = models.DateTimeField(default=now)
    nationality = models.CharField(max_length=50,  choices=AVAILABLE_COUNTRIES, default="Unknown Nationality")
    certificates = models.ManyToManyField(Certificate)


    #dodac registration date do signals zeby samo sie tworzylo przy robieniu profilu

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        min_dim = min(img.width, img.height)
        img = img.crop((0, 0, min_dim, min_dim))

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
        img.save(self.image.path)
