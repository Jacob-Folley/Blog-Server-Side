from django.db import models
from django.contrib.auth.models import User
from blogapi.models.blogger import Blogger


class BlogPost(models.Model):
    title = models.CharField(max_length=25)
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, null=True)
    summary = models.CharField(max_length=1000)
    content = models.CharField(max_length=100000)
    user = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tags", through="BlogTags", related_name='tag')