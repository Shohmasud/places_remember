from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Places(models.Model):
    name = models.CharField(max_length=500, blank=True,
                            verbose_name="NAME")
    slug = models.SlugField(max_length=500, unique=True,
                            db_index=True, verbose_name="URL")
