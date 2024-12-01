from django.db import models

# Create your models here.


class Certificate(models.Model):
    federation = models.CharField(max_length=30)
    certificate_name = models.CharField(max_length=50)
    max_depth = models.IntegerField(blank=True)