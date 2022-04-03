from django.db import models
from django.contrib.auth.models import User


class Favorites(models.Model):
    blog = models.ForeignKey("BlogPost", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)