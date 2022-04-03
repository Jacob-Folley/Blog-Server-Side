from django.db import models
from django.contrib.auth.models import User


class BlogTags(models.Model):
    tag = models.ForeignKey("Tags", on_delete=models.CASCADE)
    blog = models.ForeignKey("BlogPost", on_delete=models.CASCADE)