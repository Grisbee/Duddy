from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/app_pictures/default_profile_pic.jpg', upload_to='media/profile_pictures/')

    def __str__(self):
        return f"{self}'s profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        min_dim = min(img.width, img.height)
        img = img.crop((0, 0, min_dim, min_dim))

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
        img.save(self.image.path)