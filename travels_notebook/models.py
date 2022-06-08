from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Places(models.Model):
    name = models.CharField(max_length=500, blank=True,
                            verbose_name="NAME")
    slug = models.SlugField(max_length=500, unique=True,
                            db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name="TEXT REMEMBER")
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name="TIME CREATE")
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="TIME UPDATE")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             default=None, verbose_name="USERS")
