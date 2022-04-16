from django.db import models
from django.contrib.auth.models import User


class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
    summary = models.CharField(max_length=10000)